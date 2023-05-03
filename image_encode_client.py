# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:37:36 2023

@author: lilbl
"""

import requests
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from tkinter import filedialog
server= "http://vcm-21170.vm.duke.edu"

filename = "1489479757-baby-g-jpeg.jpg"

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
if filename is not None:
    b64_image = convert_image_file_to_base_64_str(filename)
    b64_image = view_b64_image(b64_image)


upload = {"image": b64_image, 'net_id': "tj95", "id_no": 2}
a = requests.post(server + "/add_image", json=upload)
print(a.status_code)
print(a.text)

r = requests.get(server + "/get_image/tj95/2")
print(r.status_code)
print(r.text)

view_b64_image(r.text)