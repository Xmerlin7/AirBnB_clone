#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json
''' This module is the main application'''

class HBNBCommand(cmd.Cmd):
    doc_header = 'doc_header'
    prompt = '(hbnb) '
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

    def do_EOF(self, line):
        "EXIT"
        return True

    def do_quit(Self, line):
        "EXIT"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
