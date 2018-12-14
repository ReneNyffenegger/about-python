#!/usr/bin/python3

def func():

    print("func was called")

    def nested_func():
        print("nested_func was called")

    nested_func()

func()
#
# func was called
# nested_func was called
