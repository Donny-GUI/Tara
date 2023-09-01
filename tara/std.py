import os
import sys 
import ast 


def version():
    return "".join(sys.version.split('.')[0:2])

def drive():
    return os.getcwd()[0] +":"

def libpath():
    if sys.platform.startswith('w'):
        return f"{drive()}\\Program Files\\Python{version()}\\Lib"


class Directory(object):
    def __init__(self, path:str) -> None:
        self.path = path
        self.paths = [os.path.join(self.path, x) for x in os.listdir(self.path)]
        self.directory_paths = [x for x in self.paths if os.path.isdir(x)]
        self.file_paths = [x for x in self.paths if os.path.isfile(x)]
        self.filenames = [os.path.basename(x) for x in self.file_paths]
        self.names = [os.path.splitext(x)[0] for x in self.filenames]

def stdnames():
    lpath = libpath()
    directory = Directory(lpath)
    return directory.names

def get_function_names_from_module(module_path):
    with open(module_path, 'rb') as f:
        content = f.read().decode()
    return [x.name for x in ast.walk(ast.parse(content)) if isinstance(x, ast.FunctionDef)]
    
def get_class_names_from_module(module_path):
    with open(module_path, 'rb') as f:
        content = f.read().decode()
    return [x.name for x in ast.walk(ast.parse(content)) if isinstance(x, ast.ClassDef)]

def get_class_attributes_from_module(module_path):
    classes = {}
    with open(module_path, 'rb') as f:
        content = f.read().decode()
    names = [x.name for x in ast.walk(ast.parse(content)) if isinstance(x, ast.ClassDef)]
    for name in names:
        classes[name] = {"name":name}

    for node in ast.walk(ast.parse(content)):
        if isinstance(node, ast.ClassDef):
            attrs = set()
            for cnode in ast.walk(node):
                if isinstance(cnode, ast.Attribute):
                    attrs.add(cnode.attr)
                
            classes[node.name]["attributes"] = list(attrs)
    return classes

class StandardLibrary:
    Version = version()
    Paths = sys.path
    Library = libpath()
    Files = [os.path.join(libpath(), x) for x in os.listdir(Library)]

    def object():
        return Directory(libpath())
    
    def showFilePaths():
        d = Directory(libpath())
        for x in d.file_paths:
            print(x)
    
    def show_file_paths():
        d = Directory(libpath())
        for x in d.file_paths:
            print(x)
    
    def showNames():
        d = Directory(libpath())
        for x in d.names:
            print(x)
    
    def show_names():
        d = Directory(libpath())
        for x in d.names:
            print(x)

    def getNames():
        d = Directory(libpath())
        return d.names
    
    def get_names():
        d = Directory(libpath())
        return d.names
    
    def getPaths():
        d = Directory(libpath())
        return d.file_paths

    def get_paths():
        d = Directory(libpath())
        return d.file_paths
    
    def showModuleNames():
        d = Directory(libpath())
        for x in d.names:
            print(x)

    def show_module_names():
        d = Directory(libpath())
        for x in d.names:
            print(x)

    def getModuleNames():
        d = Directory(libpath())
        return d.names
    
    def get_module_names():
        d = Directory(libpath())
        return d.names
    
    def names():
        return [x for x in Directory(libpath()).names]
    
    def get_dict():
        names = StandardLibrary.get_module_names()
        paths = StandardLibrary.get_paths()
        retv = {}
        for index, name in enumerate(names):
            retv[name] = paths[index]
        return retv
    
    def show_map():
        dict = StandardLibrary.get_dict()
        from pprint import pprint 
        pprint(dict)
    
    def full_map():
        dict = StandardLibrary.get_dict()
        for name, value in dict.items():
            path = value
            dict[name] = {}
            dict[name]['path'] = path 
            dict[name]['functions'] = get_function_names_from_module(path)
            dict[name]['classes']= {}
            dict[name]['classes']['names'] = get_class_names_from_module(path)
            dict[name]['classes']['attributes'] = get_class_attributes_from_module(path)
        return dict

    def show_full_map():
        from pprint import pprint 
        pprint(StandardLibrary.full_map())    

