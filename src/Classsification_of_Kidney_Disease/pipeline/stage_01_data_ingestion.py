from Classsification_of_Kidney_Disease.config.configuration import ConfigurationManager
from Classsification_of_Kidney_Disease.components.data_ingestion import DataIngestion
from Classsification_of_Kidney_Disease import logger

logger.info("Starting data ingestion")

STAGE_NAME = "data_ingestion"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>> {STAGE_NAME} Starting <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> {STAGE_NAME} Success <<<<")
    except Exception as e:
        logger.exception(e)
        raise e
