# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 12:06:33 2023

@author: Talya Jeter
"""
"""
def test_HDLLDL_analysis():
    from blood_calculator import HDLLDL_analysis 
    #Arrange
    HDL_input=65
    LDL_input=65
    #Act
    answer=HDLLDL_analysis(HDL_input,LDL_input)
    #Assert
    assert answer[0] == "Normal"
def test_HDLLDL_analysis_borderline_low(): 
    from blood_calculator import HDLLDL_analysis 
    #Arrange
    HDL_input=50
    LDL_input=65
    #Act
    answer=HDLLDL_analysis(HDL_input,LDL_input)
    #Assert
    assert answer[0] == "Borderline Low"
def test_HDLLDL_analysis_low(): 
    from blood_calculator import HDLLDL_analysis 
    #Arrange
    HDL_input=25
    LDL_input=65
    #Act
    answer=HDLLDL_analysis(HDL_input,LDL_input)
    #Assert
    assert answer[0] == "Low"     
"""
#OMG IT WORKED, this lets you write one test function, but test all possible
#options so it's more efficient than the above code 
import pytest 

@pytest.mark.parametrize("HDL_input, LDL_input, expected",
                         [(65,65,"Normal"),
                          (45,45,"Borderline Low"),
                          (20,20,"Low")
                          ])
def test_HDLLDL_analysis(HDL_input,LDL_input,expected):
    from blood_calculator import HDLLDL_analysis 
    #Arrange
    #Act
    answer=HDLLDL_analysis(HDL_input,LDL_input)
    #Assert
    assert answer[0] == expected

#this worked so I could test both HDL and LDL at the same time! (nature of my
#function since I had it process them both)
list_of_LDLS=[(65,120,("Normal","Normal")),
              (45,140,("Borderline Low","Borderline High")),
              (20,167,("Low","High")),
              (20,200,("Low","Very High"))]
@pytest.mark.parametrize("HDL_input, LDL_input, expected",list_of_LDLS)
def test_HDLLDL_analysis(HDL_input,LDL_input,expected):
    from blood_calculator import HDLLDL_analysis 
    #Arrange
    #Act
    answer=HDLLDL_analysis(HDL_input,LDL_input)
    #Assert
    assert answer == expected
