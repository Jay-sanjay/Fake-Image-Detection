import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Dropout, LeakyReLU
from tensorflow.keras.models import Model
from PIL import Image

image_dimensions = {'height': 256, 'width': 256, 'channels': 3}

class Classifier:
    def __init__(self):
        self.model = None
    
    def predict(self, x):
        return self.model.predict(x)
    
    def fit(self, x, y):
        return self.model.train_on_batch(x, y)
    
    def get_accuracy(self, x, y):
        return self.model.test_on_batch(x, y)
    
    def load(self, path):
        self.model.load_weights(path)

# Create a MesoNet class using the Classifier
class Meso4(Classifier):
    def __init__(self, learning_rate=0.001):
        self.model = self.init_model()
        optimizer = Adam(learning_rate=learning_rate)
        self.model.compile(optimizer=optimizer,
                           loss='mean_squared_error',
                           metrics=['accuracy'])
    
    def init_model(self): 
        x = Input(shape=(image_dimensions['height'],
                         image_dimensions['width'],
                         image_dimensions['channels']))
        
        x1 = Conv2D(8, (3, 3), padding='same', activation='relu')(x)
        x1 = BatchNormalization()(x1)
        x1 = MaxPooling2D(pool_size=(2, 2), padding='same')(x1)
        
        x2 = Conv2D(8, (5, 5), padding='same', activation='relu')(x1)
        x2 = BatchNormalization()(x2)
        x2 = MaxPooling2D(pool_size=(2, 2), padding='same')(x2)
        
        x3 = Conv2D(16, (5, 5), padding='same', activation='relu')(x2)
        x3 = BatchNormalization()(x3)
        x3 = MaxPooling2D(pool_size=(2, 2), padding='same')(x3)
        
        x4 = Conv2D(16, (5, 5), padding='same', activation='relu')(x3)
        x4 = BatchNormalization()(x4)
        x4 = MaxPooling2D(pool_size=(4, 4), padding='same')(x4)
        
        y = Flatten()(x4)
        y = Dropout(0.5)(y)
        y = Dense(16)(y)
        y = LeakyReLU(negative_slope=0.1)(y)
        y = Dropout(0.5)(y)
        y = Dense(1, activation='sigmoid')(y)

        return Model(inputs=x, outputs=y)

# Instantiate a MesoNet model with pretrained weights
meso = Meso4()
meso.load('weights/Meso4_DF.h5')

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Use the pretrained meso model
        model = meso.model

        # Load and preprocess the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(256, 256))
        test_image = image.img_to_array(test_image)
        test_image = (test_image - np.mean(test_image)) / np.std(test_image)

        # Define data augmentation
        datagen = ImageDataGenerator(
            zoom_range=0.2,        # randomly zoom into images
            rotation_range=10,     # randomly rotate images in the range (degrees, 0 to 180)
            width_shift_range=0.1, # randomly shift images horizontally (fraction of total width)
            height_shift_range=0.1,# randomly shift images vertically (fraction of total height)
            horizontal_flip=True,  # randomly flip images
            brightness_range=[0.2, 1.0], # Range for picking a brightness shift value
        )

        # Apply the augmentation defined above to the test image
        test_image = datagen.random_transform(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make prediction
        prediction = model.predict(test_image)
        result = np.round(prediction).astype(int).flatten()

        if result[0] == 1:
            prediction = 'Real'
        else:
            prediction = 'Fake'

        # Display the image and prediction in Streamlit
        img = Image.open(imagename)
        st.image(img, caption=f"Predicted: {prediction}", use_column_width=True)
        st.write(f"<h2>The Uploaded Image is: {prediction}</h2>", unsafe_allow_html=True)

        return [{"image": prediction}]