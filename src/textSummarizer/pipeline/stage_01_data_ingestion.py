from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger 

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.import_data()

if __name__ == "__main__":
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e