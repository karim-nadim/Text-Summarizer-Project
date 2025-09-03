from src.textSummarizer.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.import_data()