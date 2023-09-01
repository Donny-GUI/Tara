import sys 
from tara.type_hints import add_type_hints
from tara.train_types import train_model


class TaraCommandLineApp(object):

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
            case ("doctor",):pass
            case ("doctor", "help"):pass

    def train_model(self):
        train_model()

    def no_command(self):
        self.valueslen = len(self.set_values)
        match self.valueslen:
            case 0:self.print_help()
            case 1: self.add_type_hints(self.set_values[0])
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



