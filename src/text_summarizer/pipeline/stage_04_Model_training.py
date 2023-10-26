
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.logging import logger
from text_summarizer.components.Model_Trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()