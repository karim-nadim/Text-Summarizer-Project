from src.textSummarizer.components.model_evaluation import ModelEvaluation
from src.textSummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        model_evaluation_config = ModelEvaluation()
        model_evaluation_config.evaluate_()


if __name__=="__main__":
    STAGE_NAME = "Model Evaluation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        model_evaluation = ModelEvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e
