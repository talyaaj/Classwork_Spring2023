# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:12:04 2023

@author: lilbl
"""
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from tkinter import filedialog
from flask import Flask, request, jsonify

app = Flask(__name__)

server= "http://vcm-21170.vm.duke.edu"

# select image to upload
#def select_image():
#    filename = filedialog.askopenfilename()
#    return filename
filename = "test_image.jpg"

# convert image file to base64 string
def convert_image_file_to_base_64_str(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string
def view_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    image_buf = io.BytesIO(image_bytes)
    i = mpimg.imread(image_buf, format='JPG')
    plt.imshow(i, interpolation='nearest')
    plt.show()
    return


