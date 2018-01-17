# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:37:29 2018

@author: king
"""

import requests

from json import JSONDecoder

http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"

key ="QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"

secret ="YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"

filepath1 ="2.1.jpg"
filepath2 ="2.2.jpg"

data = {"api_key": key, "api_secret": secret, "return_landmark": "0"}

files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}

response = requests.post(http_url, data=data, files=files)

 

req_con = response.content.decode('utf-8')

req_dict = JSONDecoder().decode(req_con)

print(req_dict)