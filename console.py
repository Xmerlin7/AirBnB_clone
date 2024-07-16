#!/usr/bin/python
"""
Module for console
"""
import cmd
import re
import shlex
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.city import City
''' This module is the main application'''

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, line):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_create(self, line):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        command = shlex.split(line)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{command[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        command = shlex.split(line)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in obj.items():
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line ):
        """
        Deletes an instance based on the class name and `id`
        """
        command = shlex.split(line)
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else: 
            obj = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key in obj.items():
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        obj = storage.all()
        command = shlex.split(line)

        if len(command) == 0:
            for key, value in obj.items():
                print(str(value))
        elif command[0] in self.valid_classes:
            for key, value in obj.items():
                if key.split(".")[0] == command[0]:
                    print(str(value))
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(command[0], command[1])
            if key not in objects:
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                #if
                
                
                #else
                setattr(objects, command[2], command[3])
                storage.save()

    def default(self, line):
        """
        Default behavior for cmd module when input is invalid
        """
        line_list = line.split('.')
        cls_nm
if __name__ == '__main__':
    HBNBCommand().cmdloop()
