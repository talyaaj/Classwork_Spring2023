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
        print("1- HDL/LDL")
        print("2- Total Cholsterol")
        print("9-Quit:")
        choice= input("Select an option:")
        if choice =="9":
            keep_running= False
        elif choice =="1":
            HDLLDL_driver()
        elif choice =="2":
            chol_driver()
    print("Program ending")
#%%    
def HDLLDL_driver(): #calling all the functions together so that together they can do their job in the code
    HDL_in,LDL_in=HDLLDL_input()
    HDL_analy,LDL_analy=HDLLDL_analysis(HDL_in,LDL_in)
    HDL_output(HDL_in,HDL_analy,LDL_in,LDL_analy)
    
    
def HDLLDL_input(): 
    HDL_value = input("Enter the HDL result:")
    HDL_value = int(HDL_value)
    LDL_value=input("Enter the LDL result:")
    LDL_value=int(LDL_value)
    return HDL_value,LDL_value

def HDLLDL_analysis(HDL_int,LDL_int):
    if HDL_int>=60: 
        answer= "Normal"
    elif 40<= HDL_int<60: #in this case, the double bound is optional, but makes things easier to read
        answer="Borderline Low"
    else: 
        answer="Low"
    if LDL_int<130:
        answer2="Normal"
    elif 130<=LDL_int<=159: 
        answer2="Borderline High"
    elif 150<=LDL_int<=189: 
        answer2="High"
    else: 
        answer2="Very High"
    return answer,answer2
def HDL_output(HDL_value,HDL_analy,LDL_value,LDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value,HDL_analy))
    print("The LDL result of {} is considered {}".format(LDL_value,LDL_analy))
    return
#%%
def chol_driver(): 
    chol_in=int(chol_input())
    chol_result=chol_analysis(chol_in)
    chol_output(chol_in,chol_result)
def chol_input():
    chol_in=input("Enter the total cholesterol result:")
    return chol_in
def chol_analysis(chol_in):
    if chol_in<200:
        answer3="Normal"
    elif 200<=chol_in<=239:
        answer3="Borderline High"
    elif chol_in>=240:
        answer3="High"
    return answer3
def chol_output(chol_in,chol_result):
    print ("The total cholesterol result of {} is consdered {}".format(chol_in,chol_result))

if __name__=="__main__":
    interface()