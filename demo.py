from us_visa.logger import logging 
from us_visa.exception import USvisaException
import sys

from us_visa.pipline.training_pipeline import TrainPipeline

# try:
#     a=1/"10"
# except Exception as e:
#     logging.exception(e)
#     raise USvisaException(e,sys) from e

# from us_visa.constants import *
# print(COLLECTION_NAME)
# print(DATABASE_NAME)

pipline = TrainPipeline()

pipline.run_pipeline()

