import os
from typing import List


def get_file_paths(directory) -> List[str]:
    """
    Get all file paths in a directory.
    :param directory: str Directory path
    :return: file_paths: List[str] List of file paths
    """
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths
