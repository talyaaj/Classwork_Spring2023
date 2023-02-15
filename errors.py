# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:46:02 2023

@author: lilbl
"""

def my_function_error(rabbit):
    if rabbit <0:
        raise ValueError("You cannot send a negative number to this function"
                         " :(.")
    if type(rabbit) is str:
        raise TypeError("Cannot send a string")
    print(rabbit)

def main():
    try:
        rabbit="-3"
        my_function_error(rabbit)
    except NameError:
        print("Oops")
    except TypeError:
        rabbit=int(rabbit)
        my_function_error(rabbit)
    else:
        print("Catches all errors") #this is generally bad programming because
        #then we don't know what error was raised nor how to fix it
        #sometimes if we just want to let the user know something broke
        #without destroying the whole medical device, then this is an option
    print(answer)



if __name__=="__main__":
    main()