from src.CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from CnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
        
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "PREPARE BASE MODEL"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
        
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"********************************")
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"<<<<<<<<<<< stage {STAGE_NAME} completed")
        
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"

try:
        logger.info(f"********************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>. stage {STAGE_NAME} completed")
        
except Exception as e:
        logger.exception(e)
        raise e