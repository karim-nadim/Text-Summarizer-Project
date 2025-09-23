from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        data_transformation = DataTransformation()
        data_transformation.convert()



if __name__ == "__main__":
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e