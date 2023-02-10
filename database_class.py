# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:55:19 2023

@author: lilbl
"""
class Patient:
    def __init__(self,patient_first_name,patient_last_name,patient_mrn,patient_age):
       self.first_name=patient_first_name
       self.last_name=patient_last_name
       self.mrn=patient_mrn
       self.age=patient_age
       self.tests=[]
    def get_full_name(self):
       full_name="{} {}".format(self.first_name,
                                  self.last_name)
       return full_name
    def is_adult(self):
       if self.age>=18:
           return True
       else:
           return False
def main():
   new_patient=Patient("Ann","Ables",1,34)
   second_patient=Patient("Bob","Boyles",2,45)
   print(new_patient)
   print(second_patient)
   #new_patient.first_name="David"
   #new_patient.last_name="Ward"
   new_patient.tests.append(("HDL",100))
   print(new_patient.first_name)
   print(new_patient.last_name)
   print(new_patient.tests)
   print(new_patient.get_full_name()) #ignore the self when you call the function
   print(second_patient.first_name)
   print(new_patient.is_adult())
if __name__=="__main__":
    main()