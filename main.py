from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx===========================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Stage 02: Prepare Base Model Stage"
try:
    logger.info(f"*************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx===========================x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Stage 03: Model Training Stage"
try:
    logger.info(f"*************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<")
    training_model = ModelTrainingPipeline()
    training_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx===========================x\n")
except Exception as e:
    logger.exception(e)
    raise e