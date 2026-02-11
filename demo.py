# from src.logger import logging

# from src.exception import MyException

# import sys

print("This is a demo file to test the code execution")

from src.components.data_ingestion import DataIngestion
data_ingestion=DataIngestion()
data_ingestion.export_data_into_feature_store()
