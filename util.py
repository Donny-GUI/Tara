import os
import pickle


def import_lists():
    with open(os.getcwd()+os.sep+"data"+os.sep+"list_variables.pkl", "rb") as f:
        return pickle.load(f)

def import_booleans():
    with open(os.getcwd()+os.sep+"data"+os.sep+'boolean_variables.pkl', 'rb') as file:
        return pickle.load(file)

def import_bytes():
    with open(os.getcwd()+os.sep+"data"+os.sep+'bytes_variables.pkl', 'rb') as file:
        return pickle.load(file)

def import_dicts():
    with open(os.getcwd()+os.sep+"data"+os.sep+'dict_variables.pkl', 'rb') as file:
        return pickle.load(file)

def import_ints():
    with open(os.getcwd()+os.sep+"data"+os.sep+'int_variables.pkl', 'rb') as file:
        return pickle.load(file)

def import_strings():
    with open(os.getcwd()+os.sep+"data"+os.sep+'string_variables.pkl', 'rb') as file:
        return pickle.load(file)

BoolMap = import_booleans()
ListMap = import_lists()
BytesMap = import_bytes()
DictMap = import_dicts()
StringMap = import_strings()
IntMap = import_ints()
