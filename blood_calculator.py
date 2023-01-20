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
        print("1- HDL")
        print("9-Quit:")
        choice= input("Select an option:")
        if choice =="9":
            keep_running= False
        elif choice =="1":
            HDL_driver()
    print("Program ending")
    
def HDL_driver(): #calling all the functions together so that together they can do their job in the code
    HDL_in=HDL_input()
    HDL_analy=HDL_analysis(HDL_in)
    HDL_output(HDL_in,HDL_analy)
    
    
def HDL_input(): 
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    return HDL_value

def HDL_analysis(HDL_int):
    if HDL_int>=60: 
        answer= "Normal"
    elif 40<= HDL_int<60: #in this case, the double bound is optional, but makes things easier to read
        answer="Borderline Low"
    else: 
        answer="Low"
    return answer
def HDL_output(HDL_value,HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value,HDL_analy))
    return

interface()