import sys
import os
from tara.type_hints import add_type_hints
from tara.train_types import train_model
from tara.doctor import pull_and_patch_github_repo
from tara.remove import remove_returns, remove_type_hints, remove_type_hints_and_returns


class CommandLineApp(object):

    commands = ("train", "update", "help", "doctor", "examples")
    flags = ("-h", "-v", "-g")
    long_flags = ("--help", "--verbose", "--gui")

    def __init__(self) -> None:
        try:
            self.args = sys.argv[1:]
            self.command = self.args[0]
            print(self.command)
        except IndexError:
            self.print_help(None)
            print("  Please Provide A File Or Command  ")
            sys.exit()
        
        self.set_flags = []
        self.set_commands = []
        self.set_values = []

        for arg in self.args:
            if arg in self.commands:
                self.set_commands.append(arg)
                continue
            elif arg in self.flags or arg in self.long_flags:
                self.set_flags.append(arg)
                continue
            else:
                self.set_values.append(arg)
                continue
        self.set_flags = tuple(self.set_flags)
        self.set_commands = tuple(self.set_commands)
        self.set_values = tuple(self.set_values)
        match self.set_commands:
            case ():self.no_command()
            case ("help",):self.print_help()
            case ("help", "train"):self.print_help("train")
            case ("help", "update"):self.print_help("update")
            case ("help", "doctor"):self.print_help("doctor")
            case ("help", "examples"):self.print_help("examples")
            case ("train",):self.train_model()
            case ("train", "help"):self.print_help("train")
            case ("update",):pass
            case ("update", "help"):pass
            case ("examples",):pass
            case ("examples", "help"):pass
            case ("doctor",):self.doctor_fixes()
            case ("doctor", "help"):pass

    def ispy(self, arg: str):
        if isinstance(arg, str) and arg.endswith(".py"):
            return True
        else:
            return False

    def py_extension_panic(self, arg: str):
        if self.ispy(arg) == False:
            print("  Please Only Specify Python (.py) Files  ")
            sys.exit()

    def remove_return_types(self, arg: str):
        """ 
        Remove Return types from a given file path
         
        Arguments: arg (str) : The file path 
        
        Writes the given file to the output directory currently
        """
        self.py_extension_panic(arg)
        print("Removing Return Types...")
        new_code = remove_returns(arg)
        self.write_to_output_directory(new_code, arg)

    def write_to_output_directory(self, content: str, original_filename: str):
        file = os.path.basename(original_filename)
        example_dir = os.getcwd() + os.sep + "output"
        example = example_dir + os.sep + file
        os.makedirs(example_dir, exist_ok=True)
        with open(example, "wb") as f:
            f.write(content.encode())

    def remove_type_hints(self, arg: str):
        """ 
        Remove Type hints from a given file path
         
        Arguments: arg (str) : The file path 
        
        Writes the given file to the output directory currently
        """
        self.py_extension_panic(arg)
        print("Removing Type Hints...")
        new_code = remove_type_hints(arg)
        self.write_to_output_directory(new_code, arg)

    def doctor_fixes(self):
        print("Check-up initalized")
        print("rebuilding from source....")
        pull_and_patch_github_repo()
        print("Rebuild successfull")
        print("Retraining your models...")
        train_model()

    def train_model(self):
        train_model()

    def no_command(self):
        self.valueslen = len(self.set_values)
        match self.valueslen:
            case 0:
                self.print_help()
                print("Please Provide A Command or Python File")
                sys.exit()
            case 1: 
                self.add_type_hints(self.set_values[0])
            case other:
                for value in self.set_values:
                    self.add_type_hints(value)
    
    def add_type_hints(self, *args):
        for arg in args:
            add_type_hints(arg)

    def print_help(self, extension=None) -> None:
        print("Tara\n")
        print(" Type and Return Automaton\n")
        print("  Usage:")
        print("    tara <pythonfile>")
        print("\n  Description:")
        print("    Automated type hinting and return typing for python 3.11+")
        print("\n  Options:")
        print("    -h, --help         Show this help.")
        print("    -v, --verbose      Be loud.")
        print("    -g, --gui          Use the graphical user interface.")
        print("    -o, --output-file  Use this output file.")
        print("\n  Commands:")
        print("    add                Add type hints and/or returns to a file.")
        print("    remove             Remove type hints and/or return types from a file.")
        print("                          Keywords: 'type hints'    'types'\n\
                                                   'return types'  'returns'")
        # STOPPING POINT ************************************************************************************************
        print("    train              Train the model on your version of python3.")
        print("    update             Update the learning model")
        print("    doctor             Fix the local files and check the install")
        print("    help               Show additional information and help on a topic")
        print("    examples           Show examples of the commands and options.\n")
        match extension: 
            case "train" : pass 
            case "update" : pass 
            case "doctor" : pass
            case "examples" : pass
            case other : pass



