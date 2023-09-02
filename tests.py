from tara.app import CommandLineApp
import sys


def traintesting():
    sys.argv.append("train")
    app = CommandLineApp()


def helptest():
    sys.argv.append("help")
    app = CommandLineApp()

def updatetest():
    sys.argv.append("update")
    app = CommandLineApp()

def examplestest():
    sys.argv.append("examples")
    app = CommandLineApp()

def regulartest():
    app = CommandLineApp()

