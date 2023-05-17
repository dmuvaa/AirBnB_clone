#!/usr/bin/python3

"""creates a class for the comamand line interpreter."""

import cmd
from models.base_model import BaseModel
import models
from models import classes
import shlex


class HBNBCommand(cmd.Cmd):
    """class that contains the entry point of the command interpreter."""
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        """This methd creates a new instance of BaseModel."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            instance = classes[args[0]]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """method that prints the str rep of an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in classes:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """This method updates an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in classes:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """this method deletes an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in models.classes:
            key = args[0] + "." + args[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """This method prints the string rep of all instances."""
        args = shlex.split(arg)
        if len(args) == 0:
            for instance in models.storage.all().values():
                print(instance)
        elif args[0] in classes:
            for key, instance in models.storage.all().items():
                if args[0] in key:
                    print(instance)
        else:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """this command exits the command line."""
        return True

    def do_EOF(self, arg):
        """this command exits the command line using EoF."""
        return True

    def emptyline(self):
        """passes and empty line."""
        pass

    def default(self, arg):
        """method to hamdle class arguments."""
        args = arg.split(".")
        if len(args) > 1 and args[1] == "all()":
            self.do_all(args[0])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
