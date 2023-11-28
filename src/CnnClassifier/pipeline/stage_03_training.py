from CnnClassifier.config.configuration import ConfigurationManager
from CnnClassifier.components.prepare_callbacks import PrepareCallback
from CnnClassifier.components.training import Training 
from CnnClassifier import logger

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        config = ConfigurationManager()
        prepare_calbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_calbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list = callback_list
        )
        
if __name__ == '__main__':
    try:
        logger.info(f"********************************")
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<< stage {STAGE_NAME} completed")
        
    except Exception as e:
        logger.exception(e)
        raise e