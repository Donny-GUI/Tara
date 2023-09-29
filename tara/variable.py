
import re

# tracking and getting information about variables

def assignment_regex():
    pattern = r'(.+?)\s='
    return re.compile(pattern)

AssignRegex = assignment_regex()

def get_variable_names(filepath:str) -> list:
    retv = []
    with open(filepath, 'rb') as f:
        content = f.read().decode('utf-8')
    matches = re.finditer(pattern=AssignRegex, string=content)
    for match in matches:
        e = match.end() -2
        retv.append(match.string[match.start():e].strip())
    retv = list(set(retv))
    retv2 = []
    for item in retv:
        if " " in item:
            continue
        elif "." in item:
            continue
        elif ":" in item:
            continue
        elif "[" in item:
            continue
        retv2.append(item)
    return retv2

def determine_variable_types(variables:list[str], filepath:str):
    with open(filepath, 'rb') as f:
        content = f.read().decode('utf-8')
    vbs = [r"\b" + x + r"\b" for x in variables]
    starts = []
    ends = []    
    for vb in vbs:
        matches = re.finditer(vb)
        for match in matches:
            endindex = match.end()
            startindex = match.start()
            before, after = [], []
            stopbefore, stopafter = False, False
            while True:
                endindex+=1
                startindex-=1
                startchar, endchar = content[startindex], content[endindex]
                if stopbefore == False:
                    stopbefore = False if startchar != "\n" else True
                stopafter = False if endchar != "\n" else True
                if stopbefore is True and stopafter is True:
                    break

                char = content[index+1]


def test():
    print(get_variable_names(r"C:\Users\donald\Documents\GitHub\variable_type_hint_writer\tara\type_hints.py"))

test()