# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:00:45 2023

@author: lilbl
"""

from image_encode import convert_image_file_to_base_64_str
x = convert_image_file_to_base_64_str("test_image.jpg")
print(x[0:20])


