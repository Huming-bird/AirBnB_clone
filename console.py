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
        """ This method creates an instance from the console """

        if arg == "":
            print("** class name missing **")
        else:
            if arg == "BaseModel":
                my_model = BaseModel()
                exist = 1
            elif arg == "User":
                my_model = User()
                exist = 1
            elif arg == "State":
                my_model = State()
                exist = 1
            elif arg == "City":
                my_model = City()
                exist = 1
            elif arg == "Amenity":
                my_model = Amenity()
                exist = 1
            elif arg == "Place":
                my_model = Place()
                exist = 1
            elif arg == "Review":
                my_model = Review()
                exist = 1
            else:
                exist = 0
            if exist == 1:
                my_model.save()
                print("{}".format(my_model.id))
            else:
                print("** class doesn't exist **")

    def help_create(self):
        """ This method explains what create does """

        print('create class_name')
        print('create a new instance of class_name')

    def do_show(self, arg):
        """ This method shows the info about an instance """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.append('Amenity')
            listclass.append('Place')
            listclass.append('Review')
            if args[0] in listclass:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                ob = all_objs[obj_id]
                                print(ob)
                                find = 1
                                break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        """ This method explians what show method does """

        print('show class_name id_instance')
        print('Prints the string representation of an instance')

    def do_destroy(self, arg):
        """ this method deletes an instance from the console """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.append('Amenity')
            listclass.append('Place')
            listclass.append('Review')
            if args[0] in listclass:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                ob = all_objs[obj_id]
                                storage.destroy_objects(obj_id)
                                storage.save()
                                find = 1
                                break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_destroy(self):
        """ Thiis method explains what do destroy does """

        print('destroy class_name id_instance')
        print('Deletes an instance based on the class name and id')

    def do_all(self, arg):
        """ This method displays all instance from the json file """

        obj_list = []

        all_objs = storage.all()
        if arg == "":
            for obj_id in all_objs.keys():
                obj_list.append(str(all_objs[obj_id]))
            print(obj_list)
        else:
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.append('Amenity')
            listclass.append('Place')
            listclass.append('Review')
            if arg in listclass:
                for obj_id in all_objs.keys():
                    obj_split = obj_id.split(".")
                    if obj_split[0] == arg:
                        obj_list.append(str(all_objs[obj_id]))
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def help_all(self):
        """ This method shows what all method does """

        print('all [class_name]')
        print('Prints all string representation \
of all instances based or not on the class name')

    def do_update(self, arg):
        """ This method updates an instance """

        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split(" ")
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.append('Amenity')
            listclass.append('Place')
            listclass.append('Review')
            if args[0] in listclass:
                if len(args) < 4:
                    if len(args) == 1:
                        print("** instance id missing **")
                    if len(args) == 2:
                        print("** attribute name missing **")
                    if len(args) == 3:
                        print("** value missing **")
                else:
                    cls = args[0]
                    id_instance = args[1]
                    all_objs = storage.all()
                    find = 0
                    for obj_id in all_objs.keys():
                        obj_split = obj_id.split(".")
                        if obj_split[1] == id_instance:
                            if obj_split[0] == args[0]:
                                a1 = args[2]
                                a2 = args[3]
                                storage.update_objects(obj_id, a1, a2)
                                storage.save()
                                find = 1
                                break
                    if find == 0:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_update(self):
        """ This method explains what update method does """

        print('update class_name id_instance key value'), '\n'
        print('Updates an instance based on the class name and id \
by adding or updating attribute')

    def precmd(self, arg):
        """ This method overwrites the cmd base class method precmd """

        if '.' in arg:
            arglist = arg.split('.')
            if '(' not in arglist[1]:
                arglist2 = [arglist[1], arglist[0]]
            else:
                if 'all' in arg or 'count' in arg:
                    arglist[1] = arglist[1].replace(')', "")
                    arglist[1] = arglist[1].replace('(', "")
                    arglist2 = [arglist[1], arglist[0]]
                if 'show' in arg or 'destroy' in arg:
                    arglist[1] = arglist[1].replace(')', "")
                    arglist[1] = arglist[1].split('(')
                    arglist2 = list((arglist[1][0], arglist[0], arglist[1][1]))
                elif 'update' in arg:
                    arglist[1] = arglist[1].replace(')', "")
                    arglist[1] = arglist[1].replace('(', ",")
                    arglist[1] = arglist[1].split(",")
                    command = arglist[1][0]
                    clas = arglist[0]
                    upd_id = arglist[1][1].rstrip().lstrip()
                    upd_attr = arglist[1][2].rstrip().lstrip()
                    upd_val = arglist[1][3].rstrip().lstrip()
                    arglist2 = list((command, clas, upd_id, upd_attr, upd_val))
            arg = " ".join(arglist2)
        return cmd.Cmd.precmd(self, arg)

    def do_count(self, arg):
        """ This method counts the nummber of occurrence
        of a class instance """

        obj_list = []

        all_objs = storage.all()
        if arg == "":
            for obj_id in all_objs.keys():
                obj_list.append(str(all_objs[obj_id]))
            print(len(obj_list))
        else:
            listclass = ['BaseModel', 'User', 'City', 'State']
            listclass.append('Amenity')
            listclass.append('Place')
            listclass.append('Review')
            if arg in listclass:
                for obj_id in all_objs.keys():
                    obj_split = obj_id.split(".")
                    if obj_split[0] == arg:
                        obj_list.append(str(all_objs[obj_id]))
                print(len(obj_list))
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
