#!/usr/bin/python3

"""creates a class for the comamand line interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """class that contains the entry point of the command interpreter."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """this command exits the command line."""
        return True

    def do_EOF(self, arg):
        """this command exits the command line using EoF."""
        return True

    def emptyline(self):
        """passes and empty line."""
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
