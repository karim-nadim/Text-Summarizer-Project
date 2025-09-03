from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import get_size
from datasets import load_dataset

# I am going to only be using the import_data() method from this class

class DataIngestion:
    def __init__(self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        create_directories([self.config.data_ingestion.root_dir])

    def import_data(self):
        dataset = load_dataset("nyamuda/samsum")
        dataset.save_to_disk(f"{self.config.data_ingestion.root_dir}/samsum_dataset")
        #ds["train"].to_csv(f"{self.config.root_dir}/samsum_dataset/samsum-train.csv")
        #ds["validation"].to_csv(f"{self.config.root_dir}/samsum_dataset/samsum-validation.csv")
        #ds["test"].to_csv(f"{self.config.root_dir}/samsum_dataset/samsum-test.csv")
        logger.info("Train, Test, and Valiadation Datasets have been imported from Hugging Face")
        

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)