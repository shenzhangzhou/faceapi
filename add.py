# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 19:23:00 2018

@author: king
"""

import requests
from json import JSONDecoder

http_url2 ="https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"

key ="QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"
secret ="YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"

data2 = {"api_key": key, "api_secret": secret,"faceset_token":"644b2aed41b3d619f4109e384e5982d0",
"face_tokens":"ad68d6c220545892e4bc4d97285c1b45,851e32e7441c15a0565ecc1b43623b8b,2d60b38698943e9de075afadd1270627,9f513535f146af53c0dcebc63740559b",
"return_landmark": "0"}

response2 = requests.post(http_url2, data=data2)

req_con2 = response2.content.decode('utf-8')
req_dict2 = JSONDecoder().decode(req_con2)
print(req_dict2)