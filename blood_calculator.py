# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:25:08 2023

@author: lilbl
"""
def interface(): 
    print("Blood calculator")
    keep_running=True
    while keep_running:
        print("Options:")
        print("9-Quit:")
        choice= input("Select an option:")
        if choice =="9":
            keep_running= False
    print("Program ending")
interface()
        
