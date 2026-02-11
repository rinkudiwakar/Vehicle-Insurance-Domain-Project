# from src.logger import logging

# from src.exception import MyException

# import sys

print("This is a demo file to test the code execution")

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()

