import sys
from XRAY.cloud_storage.s3_operations import s3operation
from XRAY.entity.artifact_entity import DataIngestionArtifact
from XRAY.entity.config_entity import DataIngestionConfig
from XRAY.exception import XRAYException
from XRAY.logger import logging

class data_ingestion():
    def __init__(self):
        pass
    def get_data_from_s3(self):
        try:
            pass
        except Exception as e:
            raise XRAYException(e,sys)
    def Initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRAYException(e, sys)