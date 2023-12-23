import sys 
from tara.type_hints import add_type_hints
from tara.train_types import train_model
from tara.doctor import pull_and_patch_github_repo

GREEN = "\033[32m"
GREENBG = "\033[42m"
RED = "\033[31m"
REDBG = "\033[41m"
RC = "\033[0m"
BLUE = "\033[33m"
BLUEBG = "\033[43m"

def details_print(details: str):
    if isinstance(details, list):
        for line in details:
            print("             ",  GREEN + line + RC)
    elif isinstance(details, str):    
        lines = details.split("\n")
        for line in lines:
            print("             ",  GREEN + details + RC)

def error_print(error):
    print(REDBG + " Error  Call " + RC,  RED + error + RC)

def method_print(method):
    print(GREENBG + " Method Call " + RC,  GREEN + method + RC)

def method_end(method):
    print(GREENBG + " Method  End " + RC, GREEN + method + RC)

def exit_print(sys=True):
    line = ""
    if sys:
        line = " System Exit "
    else:
        line = "    Exit     "
    print(BLUEBG + RED + line + RC)

class CommandLineApp(object):

    commands = ("train", "update", "help", "doctor", "examples")
    flags = ("-h", "-v", "-g")
    long_flags = ("--help", "--verbose", "--gui")

    def __init__(self) -> None:

        method_print("CommandLineApp.__init__(self)")

        try:
            self.args = sys.argv[1:]
            self.command = self.args[0]
            print("Command: ", self.command)
        except IndexError:
            error_print("CommandLineApp.__init__  IndexError")
            details_print(["[] System Arguments", " ".join(sys.argv)])
            self.print_help(None)
            exit_print()
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
        method_end("CommandLineApp.__init__(self)")

    def doctor_fixes(self):

        method_print("CommandLineApp.doctor_fixes(self)")

        print("Check-up initalized")
        print("rebuilding from source....")
        pull_and_patch_github_repo()
        print("Rebuild successfull")
        print("Retraining your models...")
        train_model()

        method_end("CommandLineApp.doctor_fixes(self)")

    def train_model(self):

        method_print("CommandLineApp.train_model(self)")

        train_model()

        method_end("CommandLineApp.train_model(self)")

    def no_command(self):

        method_print("CommandLineApp.no_command(self)")

        self.valueslen = len(self.set_values)
        match self.valueslen:
            case 0:
                self.print_help()
            case 1: 
                self.add_type_hints(self.set_values[0])
            case other:
                for value in self.set_values:
                    self.add_type_hints(value)
        method_end("CommandLineApp.no_command(self)")
    
    def add_type_hints(self, *args):

        method_print("CommandLineApp.add_type_hints(self, *args)")

        for arg in args:
            add_type_hints(arg)
        method_end("CommandLineApp.add_type_hints(self, *args)")

    def print_help(self, extension=None) -> None:

        method_print(f"CommandLineApp.print_help(self, extension={extension})")

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

        method_end(f"CommandLineApp.print_help(self, extension={extension})")
