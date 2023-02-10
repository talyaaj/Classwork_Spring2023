# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:55:19 2023

@author: lilbl
"""
class Patient: 
    def __init__(self):
       self.first_name=""
       self.last_name=""
       self.mrn=0
       self.age=0
       self.tests=[]
def main():
   new_patient=Patient()
   second_patient=Patient()
   print(new_patient)
   print(second_patient)
   new_patient.first_name="David"
   new_patient.last_name="Ward"
   new_patient.tests.append(("HDL",100))
   print(new_patient.first_name)
   print(new_patient.last_name)
   print(new_patient.tests)
   print(second_patient.first_name)   
if __name__=="__main__":
    main()