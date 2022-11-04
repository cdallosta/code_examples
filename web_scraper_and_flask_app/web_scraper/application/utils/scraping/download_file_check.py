from os import listdir, path
from time import sleep


def download_wait(path_to_directory: str, timeout_sec: int = 30) -> str:
    """
    Iterates until the iterator has reached the timeout_sec argument.
    On each iteration it extracts the directory content and checks to
    if the given file_name is present. Returns a boolean of the result

    Args:
        path_to_directory (str): path to the directory to watch
        timeout_sec (int): the max amount of time to look for the
        given file_name

    Returns:
        str: the file name
    """
    # "_" used to indicate an unused variable
    for _ in range(0, timeout_sec, 1):
        directory = listdir(path_to_directory)
        if len(directory) > 0:
            return directory[0]
        sleep(1)
    return ""
