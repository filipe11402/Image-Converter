import requests
import base64


BASE = 'http://127.0.0.1:5000/'

with open('test.jpg', 'rb') as f_img:
    img_b64 = base64.b64encode(f_img.read())

""" response = requests.post(BASE + 'teste/1/', {'img_b64': img_b64, 'new_size': 60}) """ # sending data to create image and the new size
"""response = requests.get(BASE + 'teste/1/')"""  # GET request to get the Photo

print(response.json())