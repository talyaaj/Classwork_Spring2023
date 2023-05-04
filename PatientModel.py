# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:19:41 2023

@author: lilbl
"""

from pymodm import MongoModel, fields

class Patient(MongoModel):
    patient_id = fields.IntegerField(primary_key=True)
    patient_name = fields.CharField()
    blood_type = fields.CharField()
    tests = fields.ListField()