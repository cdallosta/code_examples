import logging
import os

logger=logging.getLogger(__name__)

def rm_directory_file(directory_path: str) -> None:
    """Takes in a directory path and removes all file

    Args:
        directory_path (str): the directory to clear
    """
    for f in os.listdir(directory_path):
        os.remove(os.path.join(directory_path, f))
        logger.info(f"{f} deleted")
        
