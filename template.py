import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(funcName)s: %(message)s')

project_name = "TextSummarizer"

files_list = [  ".github/workflows/.gitkeep",
                f"src/{project_name}/__init__.py",
                f"src/{project_name}/components/__init__.py",
                f"src/{project_name}/utils/__init__.py",
                f"src/{project_name}/utils/common.py",
                f"src/{project_name}/config/__init__.py",
                f"src/{project_name}/config/configuration.py",
                f"src/{project_name}/logging/__init__.py",
                f"src/{project_name}/pipeline/__init__.py",
                f"src/{project_name}/entity/__init__.py",
                f"src/{project_name}/constants/__init__.py",
                "config/config.yaml",
                "params.yaml",
                "app.py",
                "setup.py",
                "main.py",
                "Dockerfile",
                "requirements.txt",
                "research/trials.ipynb"
              ]

for file in files_list:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file : {file_path}")
    else:
        logging.info(f"Already existing path, so not creating : {file_path}")


