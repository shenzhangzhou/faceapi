# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:06:13 2018

@author: king
"""

import cv2
import requests
from json import JSONDecoder

http_url1 ="https://api-cn.faceplusplus.com/facepp/v3/faceset/create"


key ="QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"
secret ="YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"

data1 = {"api_key": key, "api_secret": secret,"return_landmark": "0"}

response1 = requests.post(http_url1, data=data1)

req_con1 = response1.content.decode('utf-8')

req_dict1 = JSONDecoder().decode(req_con1)


print(req_dict1)

