from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_ingestion import DataIngestion
from TextSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion = DataIngestion(config=config_manager.getDataIngestionConfig())
        data_ingestion.download_file()
        data_ingestion.extract_zip()