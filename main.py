from Classsification_of_Kidney_Disease import logger
from  Classsification_of_Kidney_Disease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from  Classsification_of_Kidney_Disease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Classsification_of_Kidney_Disease.pipeline.stage_03_model_training import ModelTrainingPipeline
from Classsification_of_Kidney_Disease.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "data_ingestion"

try:
    logger.info(f">>>> {STAGE_NAME} Starting <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> {STAGE_NAME} Success <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "prepare_base_model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Train model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluate model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
