import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]

for filePath in list_of_files:
    filePath = Path(filePath)
    filedir, filename = os.path.split(filePath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory: {filedir} For file: {filename}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
    else:
        logging.info(f"File already exists: {filePath}")

