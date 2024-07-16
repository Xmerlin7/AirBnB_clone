#!/usr/bin/env python3
import cmd
''' This module is the main application'''

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    def do_EOF(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()