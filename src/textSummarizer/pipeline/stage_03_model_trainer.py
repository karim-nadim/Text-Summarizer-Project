from src.textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        model_trainer_config = ModelTrainer()
        model_trainer_config.train()