import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s:%(message)s]')

project_name="text_summarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/enetity/__init__.py",
    f"src/{project_name}/constants/__init__.py",\
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "reseach/trail.ipynb"
]


for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,filename=os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Created directory {file_dir} for the file {filename}")
    
    if (not  os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Created empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")