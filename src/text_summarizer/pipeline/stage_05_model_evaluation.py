
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.logging import logger
from text_summarizer.components.model_evaluation import ModelEvaluation
class modelevaluationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()