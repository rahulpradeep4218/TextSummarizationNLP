import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml( file_path: Path) -> ConfigBox:
    """
    Reads YAML files when we pass the path of the YAML file
    Returns ConfigBOX object
    """
    try:
        with open(file_path) as f:
            contents = yaml.safe_load(f)
            logger.info(f"YAML File : {file_path} loaded successfully")
            return ConfigBox(contents)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(paths:list, verbose=True):
    """
    Craetes directories for the paths send in the list arg
    Verbose argument to indicate if logging required, defaults to True
    """
    for dir in paths:
        os.makedirs(dir, exist_ok=True)
        if verbose:
            logger.info(f"Created directory : {dir}")


@ensure_annotations
def get_size(path:Path) -> str:
    size_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_kb} KB"