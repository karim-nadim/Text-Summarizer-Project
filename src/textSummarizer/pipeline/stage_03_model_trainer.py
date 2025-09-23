from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer.logging import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        model_trainer_config = ModelTrainer()
        model_trainer_config.train()

if __name__ == "__main__":
    STAGE_NAME = "Model Training stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e