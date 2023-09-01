
import ast 
from ast import Name
import os
import pickle
from string import ascii_letters


class SequenceType:
    List = list
    Range = range
    Tuple = tuple
    Names = ["list", "range", "tuple"]

class NumericType:
    Integer = int
    Decimal = float 
    Complex = complex 

class BinaryType:
    Bytes = bytes
    ByteArray = bytearray
    MemoryView = memoryview  

class BooleanType:
    Bool = bool

class SetType:
    Set = set
    FrozenSet = frozenset

class PythonVariable:
    Names = ["list", "range", "tuple", "int", "float", "complex", "str", "bytes", "bytearray", "memoryview", "bool", "set", "frozenset", "dict"]
    Types = [list, range, tuple, int, float, complex, str, bytes, bytearray, memoryview, bool, set, frozenset, dict]


import importlib 

class Importer(object):
    def __init__(self) -> None:
        self.module = None
        self.function_names = []
        self.map = {}
    
    def load(self, module_name:str):
        try:
            self.module = importlib.import_module(module_name)
            self.function_names = [name for name in dir(self.module) if callable(getattr(self.module, name))]
        except ImportError as e:
            print(f"failed to load module {e}")


class PythonFile:
    def classNames(filepath:str):
        class_names = []

        with open(filepath, 'r') as file:
            tree = ast.parse(file.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_names.append(node.name)

        return class_names

    def inheritedClassNames(filepath:str):
        classes = {}
        names = []
        with open(filepath, 'r') as file:
            tree = ast.parse(file.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name not in names:
                        classes[node.name] = []
                        names.append(node.name)
                    for base in node.bases:
                        if isinstance(base, ast.Name):
                            classes[node.name].append(base.id)
        return classes

class TypeNode:
    INT  = Name(id=int, name="int")
    STR  = Name(id=str, name="str")
    LIST = Name(id=list, name="list")
    DICT = Name(id=dict, name="dict")
    SET  = Name(id=set, name="set")
    NONE = Name(id=None, name="None")
    ALL  = [INT, STR, LIST, DICT, SET]
    
    def of(type:str):
        for t in TypeNode.ALL:
            if t.name == type:
                return t
            

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
All = [StringMap, IntMap, BoolMap, ListMap, DictMap, BytesMap]


class PythonType:
    Names = ['str', 'int', 'dict', 'list', 'set', 'memoryview', 'bytes', 'bytearray', 'tuple', 'float', 'complex']
    Literals = [str, int, dict, list, set, memoryview, bytes, bytearray, tuple, float, complex]
    StringTags = ['"', "'", "str(", "f'", 'f"']

    def check(object) -> bool:
        for l in Types.Literals:
            if isinstance(object, l):
                return True
        return False
    
    def which(object) -> str:
        for index, l in enumerate(PythonType.Literals):
            if isinstance(object, l):
                return PythonType.Names[index]
        return None
    
    def evaluate_string_literal(string:str) -> str:
        
        def is_string(string:str) -> bool:
            
            for x in PythonType.StringTags:
                if string.startswith(x):
                    return True
            if string.endswith('"') or string.endswith("'"):
                return True
            return False

        def is_dict(string:str) -> bool:
            obj = string.strip(" ")
            if obj.startswith("{"):
                return True
            elif obj.endswith("}"):
                return True
            if obj.startswith("dict("):
                return True
            testvar = ""
            for char in obj:
                testvar+=char
                if char not in ascii_letters:
                    if char =="[" and len(testvar) > 1:
                        return True
            return False

        def is_bytes(string:str):
            if string.startswith("bytes(") or string.startswith("0x") or string.startswith("b'") or string.startswith('b"'):
                return True
            return False
        
        def is_bytes_array(string:str):
            if string.startswith("bytearray("):
                return True
            return is_bytes(string)
        
        def is_tuple(string:str):
            tags = "tuple(", "("
            for t in tags:
                if string.startswith(t):
                    return True
            
            commacount = string.count(",")
            quotecount = string.count('"')
            squotecount = string.count("'")
            if commacount > 0:
                if quotecount > 0 or squotecount > 0:
                    return True
            return False

        def is_int(string:str):
            stripped = string.strip(" ")
            if stripped[0] in "123456789":
                return True
            elif stripped.startswith("int(") and stripped.startswith("len("):
                return True
    
        funcs = [is_string, is_int, is_bytes, is_bytes_array, is_dict, is_tuple]
        names = ["string", "int", "bytes", "bytes_array", "dict", "tuple"]
        stripped = string.strip(" ")
        for index, fun in enumerate(funcs):
            if fun(stripped) == True:
                return names[index]
        return None

class Var:

    def identifyType(variable:str):
        for varT in All:
            try:
                return varT[variable]
            except KeyError:
                continue
        return None


mathsyms = "%+=->*^!<./|\\"
punctsys = "?;:'~" +'"'
digitsyms = "0123456789"

class CharacterNode:
    def __init__(self, index, char, nextchar, lastchar) -> None:
        self.char: str = char
        self.index: int = index
        self.nextchar: str = nextchar
        self.lastchar: str = lastchar
        self.isfinal: bool = False
        self.isrepeated: bool = False if self.lastchar != self.char else True
        self.willrepeat: bool = False if self.nextchar != self.char else True
        self.endword: bool = True if self.lastchar != self.char and self.char in "_ " else False
        self.startword: bool = True if self.nextchar != self.char and self.char in "_ " else False
        self.uppercaseStart: bool = True if self.lastchar.islower() and self.char.isupper() else False
        self.uppercaseEnd: bool = True if self.lastchar.isupper() and self.char.islower() else False
        self.possible = 30
        self.subtype = "Unknown"
        if char in mathsyms:
            self.chartype = "math"
        elif char in punctsys:
            self.chartype = "punct"
        elif char in digitsyms:
            self.chartype = "digit"
        elif char in ascii_letters:
            self.chartype = "letter"
        elif self.char in "_ ":
            self.chartype = "whitespace"
        else:
            self.chartype = "?"
        if self.chartype == "letter":
            if self.char.isupper() == True:
                self.subtype = "uppercase"
            else:
                self.subtype = "lowercase"
        elif self.chartype == "math":
            if self.char in "+-/*=":
                self.subtype = "algebraic"
            elif self.char in "$%.,":
                self.subtype = "currency"
        elif self.chartype == "digit":
            if self.char in "13579":
                self.subtype = "odd"
            elif self.char in "02468":
                self.subtype = "even"
    
    def compare(self, node):
        if not isinstance(node, CharacterNode):
            print("ERROR not a character node.")
            exit()
        node: CharacterNode
        self.score = 0
        if node.char == self.char:
            self.score+=3
        elif node.nextchar == self.nextchar:
            self.score+=2
        elif node.lastchar == self.lastchar:
            self.score+=2
        elif node.lastchar == self.char:
            self.score+=2
        elif node.nextchar == self.char:
            self.score+=2
        elif self.chartype == node.chartype:
            self.score+=2
        elif self.subtype == node.subtype:
            self.score+=3
        elif self.isfinal == node.isfinal:
            self.score+=4
        elif self.isrepeated == node.isrepeated:
            self.score+=1
        elif self.willrepeat == node.willrepeat:
            self.score+=2
        elif self.endword == node.endword:
            self.score+=3
        elif self.startword == node.startword:
            self.score+=2
        elif self.uppercaseStart == node.uppercaseStart:
            self.score+=1
        elif self.uppercaseEnd == node.uppercaseEnd:
            self.score+=1
        return self.score
    
def create_gradient():
    gradient = []
    
    for i in range(0, 256):
        r = min(i, 255)
        g = min(255 - i, 255)
        b = 0
        gradient.append(f"\x1b[48;2;{r};{g};{b}m ")
    retv = []
    for i in range(0, 255):
        num = 255-i
        retv.append(gradient[num])
    return retv

class Sentence(object):
    grad = create_gradient()

    def __init__(self, string:str) -> None:
        
        self.string = string
        self.characters = [x for x in self.string]
        self.slices = []
        self.length = len(self.characters)
        self.head = CharacterNode(index=0, char=self.characters[0], lastchar="None", nextchar=self.characters[1])
        self.nodes = [self.head, ]
        for i in range(0, len(self.string)-1):
            if i == 0:pass
            if i == self.length:pass
            sl = [i-1, i, i+1]
            sla = (self.characters[sl[0]], self.characters[sl[1]], self.characters[sl[2]])
            self.nodes.append(CharacterNode(char=sla[1], index=i, nextchar=sla[2], lastchar=sla[0]))
        self.tail = CharacterNode(index=-1, nextchar="None", char=self.characters[-1], lastchar=self.characters[-2])
        self.nodes.append(self.tail)
        self.scores = []
        self.perc_thirty = 10
        
    def compare(self, string:str):
        self.scores = []
        opSent = Sentence(string=string)
        for index, node in enumerate(self.nodes):
            score = node.compare(opSent.nodes[index])
            self.scores.append(score)
        


def test():
    sen = Sentence("This code extends the previous example by adding functionality to determine word count")
    sen.compare("Adjust the input_str variable to analyze different strings. Keep in mind that identifying words, numbers, and built-in names might have various interpretations and requirements based on your specific needs.")
    
test()