import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: {headers}")
        else:
            logger.info(f"File already exists with file size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(file=self.config.local_data_file, mode='r') as zipRef:
            zipRef.extractall(unzip_dir)
        logger.info("Extraction of file complete")