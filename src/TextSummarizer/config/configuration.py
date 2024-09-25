from TextSummarizer.constants import *
from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH, param_path = PARAM_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml( param_path)
        create_directories([self.config.artifacts_root])

    def getDataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir=config.root_dir, 
            source_URL=config.source_URL, 
            local_data_file=config.local_data_file, 
            unzip_dir=config.unzip_dir
        )
    
    