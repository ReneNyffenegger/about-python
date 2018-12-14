#!/usr/bin/python3

def func():

    print("func was called")

    def nested_func():
        print("nested_func was called")

        def doubly_nested_func():
            print("doubly_nested_func was called")

        doubly_nested_func()

    nested_func()

func()
#
# func was called
# nested_func was called
# doubly_nested_func was called
