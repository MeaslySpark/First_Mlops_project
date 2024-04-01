import os
from pathlib import Path

list_of_files = [

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",  #here we added components file in src file which will collection of all the components in Mlops pipeline
    "src/components/data_ingestion.py",  #all the code here
    "src/components/data_transformation.py", 
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py", #utilities
    "src/logger/logging.py",
    "src/exception/exception",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "experiment/experiments.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file