#!/usr/bin/env python3

import requests
import os


# This example shows how a file can be uploaded using
# The Python Requests module
url = "http://localhost/upload/"
IMAGES_DIR = os.path.expanduser('~') + '/supplier-data/images/'
list_image = os.listdir(IMAGES_DIR)
jpg_images = [image_name for image_name in list_image if '.jpeg' in image_name]

for image in jpg_images:
  with open(IMAGES_DIR + image, 'rb') as opened:
    r = requests.post(url, files={'file': opened})