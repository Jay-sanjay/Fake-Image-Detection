import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.config.configuration import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    

    def get_base_model(self):
        # Load the base model
        base_model = tf.keras.models.load_model(self.config.updated_base_model_path)

        # Create a new model that includes all layers of the base model except the last one
        inputs = base_model.input
        x = base_model.layers[-2].output

        # Add a new last layer that matches the number of classes
        outputs = tf.keras.layers.Dense(2, activation='softmax')(x)

        # Create the new model
        self.model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
        
        
    # From Keras documentations
    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # if self.config.params_is_augmentation:
        #     train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
        #         rotation_range=40,
        #         horizontal_flip=True,
        #         width_shift_range=0.2,
        #         height_shift_range=0.2,
        #         shear_range=0.2,
        #         zoom_range=0.2,
        #         **datagenerator_kwargs
        #     )
        # else:
        train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)



    # def save_model(self, path: Path):
    #     self.model.save(path)

    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        # Create a new optimizer instance
        optimizer = tf.keras.optimizers.Adam()

        # Compile the model with the new optimizer
        self.model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )