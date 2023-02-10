# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:18:19 2023

@author: lilbl
"""
#%%
def create_patient_entry(patient_fname,patient_lname,patient_mrn,patient_age):
    #new_patient=[patient_name,patient_mrn,patient_age,[]] #empty list serves as a place to store tests 
    new_patient={"First Name":patient_fname, "Last Name":patient_lname,"MRN":patient_mrn, "Age":patient_age, "Tests":[]} 
    return new_patient
def main_driver():
    db=[]
    db.append(create_patient_entry("Ann","Ables",1,34))
    db.append(create_patient_entry("Bob","Boyles",2,45))
    db.append(create_patient_entry("Chris","Chou",3,52))
    print(db)
    add_test_to_patient(db,1,"HDL",120)
    add_test_to_patient(db,2,"LDL",100)
    room_numbers=["103","232","333"]
    print(db)
    print_directory(db,room_numbers)
    mrn_to_find=2
    test_name="HDL"
    check_test(db,mrn_to_find,test_name)
    return 
#%%
def check_test(db,mrn_to_find,test_name):
    patient=get_patient_entry(db,mrn_to_find)
    for x in patient[3]:
        if x[0]==test_name:
            print("The patient's "+test_name+" yielded a value of "+str(x[1]))
        else: 
            print("The patient did not have a test for "+test_name)
    return 
#%%
def print_directory(db,room_numbers):
    for i, patient in enumerate(db):  #i stores the index variable (so it's like count, but not manual)
        print(("Patient {} is in room {}").format(patient[0],room_numbers[i]))
    for patient,rn in zip(db,room_numbers):  #this works because they're two lists of the same length 
        print(("Patient {} is in room {}").format(patient[0],rn))
#%%
def get_patient_entry(db,mrn_to_find): #this function doesn't know the variable db, 
#but it knows to call whatever the first entry to it db 
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False
def add_test_to_patient(db,mrn_to_find,test_name,test_value):
    patient=get_patient_entry(db,mrn_to_find)
    if patient is False: 
        print("Bad entry ")
    else: 
        patient[3].append([test_name,test_value])
    return 
#%%    
if __name__=='__main__':
    main_driver()