from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):
        
        self.config = read_yaml(config_filepath)

    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_evaluation.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_evaluation.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output