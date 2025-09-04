from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import torch

class ModelTrainer:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
        create_directories([self.config.model_trainer.root_dir])


    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_trainer.model_ckpt)
        model_distilbart = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_trainer.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_distilbart)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.model_trainer.data_path)

        params = self.params.TrainingArguments

        trainer_args = TrainingArguments(
            output_dir=self.config.model_trainer.root_dir, num_train_epochs=params.num_train_epochs, 
            warmup_steps=params.warmup_steps, 
            per_device_train_batch_size=params.per_device_train_batch_size, 
            per_device_eval_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay, logging_steps=params.logging_steps,
            eval_strategy=params.evaluation_strategy, eval_steps=params.eval_steps, 
            save_steps=params.save_steps, 
            gradient_accumulation_steps=params.gradient_accumulation_steps,

            logging_dir=os.path.join(self.config.model_trainer.root_dir, "logs"),
            logging_first_step=True,
            log_level="info",
            report_to=[] 
        ) 



        trainer = Trainer(model=model_distilbart, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        ## Save model
        model_distilbart.save_pretrained(os.path.join(self.config.model_trainer.root_dir,"distilbart-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.model_trainer.root_dir,"tokenizer"))
