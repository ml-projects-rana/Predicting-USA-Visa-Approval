import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [

    f"{project_name}/__init__.py", 
#constructor file required because us_visa folder will act like a local package. 
#Whenever setup.py is executed since we are looking for requirements at that time us_visa folder installed as local package
    f"{project_name}/components/__init__.py",  
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",   #Creating .yaml file inside config folder
    "config/schema.yaml",


]


for filepath in list_of_files:
    #Detect the machine (window/linux/mac) you're working and accordingly change the forward / backward slash so that path is not a problem while working.
    filepath = Path(filepath)
    #This line uses the os.path.split() function to split the file path into its directory and file name components.
    filedir, filename = os.path.split(filepath)
    """ 
    This block of code checks if the directory component of the file path is not empty. 
    If it's not empty, it creates the directory (along with any necessary parent directories) using os.makedirs() function. 
    The exist_ok=True argument ensures that the function does not raise an error if the directory already exists. 
    """
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    #This line checks if the file does not exist (os.path.exists()) or if its size is zero (os.path.getsize()). 
    #If either condition is true, it means the file is either missing or empty

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        #If the file does not exist or is empty, this block of code opens the file in write mode ("w") and then immediately closes it without writing anything. 
        #This effectively creates an empty file.
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")



