#!/usr/bin/python3
""" This module holds our console source code """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


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
        """ This method creates a class instance using
        console command """

        class_list = ['BaseModel', 'User', 'City', 'State']
        listclass.extend(['Amenity', 'Place', 'Review'])

        if arg:
            if arg in class_list:
                my_model = eval(arg)()
                my_model.save()
                print("{}".format(my_model.id))
            else:
                print("** class doesn't exist **")
        else:
            print("** clss name is missing **")

    def help_create(self):
        """ This method shows what create method does """

        print('create class_name'), '\n'
        print('create a new instance of class_name')

    def do_show(self, arg):
        """ This method shows the string rep of an instance """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")

            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.extend(['Amenity', 'Place', 'Review'])

            if len(args) < 2:
                print("** instance id missing **")
            else:
                if args[0] in listclass:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    found = False
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                ob = all_objs[obj_id]
                                print(ob)
                                found = True
                                break
                    if not found:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def help_show(self):
        """ This method displays what show methodo does """

        print('show class_name id_instance'), '\n'
        print('Prints the string representation of an instance')

    def do_destroy(self, arg):
        """ This method deletes an instance of a class """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")

            listclass = ['BaseModel', 'User', 'City', 'State']
            listclas.extend(['Amenity', 'Place', 'Review'])

            if len(args) < 2:
                print("** instance id missing **")
            else:
                if args[0] in listclass:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    found = False
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                ob = all_objs[obj_id]
                                storage.destroy_objects(obj_id)
                                storage.save()
                                found = True
                                break
                    if not found:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def help_destroy(self):
        """ This method describes what destroy method does """

        print('destroy class_name id_instance'), '\n'
        print('Deletes an instance based on the class name and id')

    def do_all(self, arg):
        """ This method shows all str rep of all instances """

        all_objs = storage.all()
        if arg == "":
            for obj_id in all_objs.keys():
                print(all_objs[obj_id])
        else:
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.extend(['Amenity', 'Place', 'Review'])

            if arg in listclass:
                for obj_id in all_objs.keys():
                    obj_split = obj_id.split(".")
                    if obj_split[0] == arg:
                        print(all_objs[obj_id])
            else:
                print("** class doesn't exist **")

    def help_all(self):
        """ This method shows what the all method does """

        print('all [class_name]'), '\n'
        print('Prints all string representation \
of all instances based or not on the class name')

    def do_update(self, arg):
        """ This method updates an instance based on class command """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.extend(['Amenity', 'Place', 'Review'])

            if len(args) == 1:
                print("** instance id missing **")
            if len(args) == 2:
                print("** attribute name missing **")
            if len(args) == 3:
                print("** value missing **")
            else:
                if arg[0] in listclass:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = False
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                a1 = args[2]
                                a2 = args[3]
                                storage.update_objects(obj_id, a1, a2)
                                storage.save()
                                find = True
                                break
                    if not find:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def help_update(self):
        """ This method explains what update method does """

        print('update class_name id_instance key value'), '\n'
        print('Updates an instance based on the class name and id \
by adding or updating attribute')


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
