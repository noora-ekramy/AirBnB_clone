#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    storage = FileStorage()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        try:
            print(self.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        try:
            del self.storage.all()[key]
            self.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        if arg:
            try:
                eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(obj) for obj in self.storage.all().values()])

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute"""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not arg else "** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in self.storage.all().keys():
            print("** no instance found **")
            return
        obj = self.storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
