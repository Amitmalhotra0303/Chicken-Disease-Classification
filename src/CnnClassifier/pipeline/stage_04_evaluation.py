from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier.components.evaluation import Evaluation
from CnnClassifier import logger

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
if __name__ == '__main__':
    try:
        logger.info(f"********************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>. stage {STAGE_NAME} completed")
        
    except Exception as e:
        logger.exception(e)
        raise e