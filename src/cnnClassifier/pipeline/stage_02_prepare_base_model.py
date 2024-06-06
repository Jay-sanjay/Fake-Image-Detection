from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = 'Prepare Base Model'


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.load('/home/jay-sanjay/Downloads/weights/Meso4_DF.h5')
        prepare_base_model.update_base_model()
    

if __name__ == '__main__':
    try:
        logger.info(f"*************************")
        logger.info(f" >>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<< ")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f" >>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<< ")
    except Exception as e:
        logger.error(f"Stage: {STAGE_NAME} failed with error: {str(e)}")
        raise e