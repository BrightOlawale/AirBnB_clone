#!/usr/bin/python3


def welcome():
    name = input("What is your name?\n")
    text = "have fun going through the program"
    return "Welcome " + name + " to my Airbnb project, " + text + "!"

def missing():
    print("** class name missing **")
    return

def idmissing():
    print("** instance id missing **")
    return

def cls_d_exist():
    print("** class doesn't exist **")
    return

def no_instance():
    print("** no instance found **")
    return