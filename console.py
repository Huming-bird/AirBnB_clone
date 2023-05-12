#!/usr/bin/python3
""" This module holds our console source code """

import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """ This is the blue print for our console class """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ This method exits the console """

        return True

    def do_EOF(self, arg):
        """ This method exits the console """

        return True

    def emptyline(self):
        """ Overriding base class method to do nothing """
        pass

    def do_create(self, arg):
        """ This console method will create class objects """

        # checks if arg is present
        if arg:
            if arg == "BaseModel":
                new_object = BaseModel()
                new_object.save()

                print(new_object.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name is missing **")

    def do_show(self, arg):
        """ This method prints the str rep of an object """

        print(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
