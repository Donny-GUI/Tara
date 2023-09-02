import os
import sys
from dataclasses import dataclass as dcls
import git
import shutil


TARAPATH = os.getcwd()
ROOTPATH = os.sep.join(TARAPATH.split(os.sep)[:-1])

@dcls(slots=True)
class Path:
    Tara     = TARAPATH
    Root     = ROOTPATH
    Output   = os.path.join(ROOTPATH, "output")
    Data     = os.path.join(ROOTPATH, "data")
    Examples = os.path.join(ROOTPATH, "examples")
    BOOLEAN  = os.path.join(ROOTPATH, "data", "boolean_variables.pkl")
    BYTES    = os.path.join(ROOTPATH, "data", "bytes_variables.pkl")
    DICT     = os.path.join(ROOTPATH, "data", "dict_variables.pkl")
    FLOAT    = os.path.join(ROOTPATH, "data", "float_variables.pkl")
    INT      = os.path.join(ROOTPATH, "data", "int_variables.pkl")
    LIST     = os.path.join(ROOTPATH, "data", "list_variables.pkl")
    STR      = os.path.join(ROOTPATH, "data", "string_variables.pkl")
    Main     = os.path.join(ROOTPATH, "main.py")
    Exe      = os.path.join(ROOTPATH, "tara.exe")
    ALL = (
        Tara, Root, Output, Data, Examples, BOOLEAN, BYTES, DICT, FLOAT, INT, LIST, STR, Main, Exe
    )

def pull_and_patch_github_repo(repository_url="https://github.com/Donny-GUI/Tara.git"):
    """
    Pulls source code from a GitHub repository and applies it to the current working directory.
    Parameters:
        repository_url (str): The URL of the GitHub repository to pull from.
    Returns:
        bool: True if the operation is successful, False otherwise.
    """
    try:
        temp_dir = os.path.join(os.getcwd(), "tmp")
        repo = git.Repo.clone_from(repository_url, temp_dir)
        # Copy the contents of the cloned repository to the current working directory
        for root, _, files in os.walk(temp_dir):
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(os.getcwd(), os.path.relpath(src_file, temp_dir))
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)
        shutil.rmtree(temp_dir)
        git.Repo(os.getcwd()).index.add("*")
        git.Repo(os.getcwd()).index.commit("GitHub pull")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


    



