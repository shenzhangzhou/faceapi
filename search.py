# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:56:12 2018

@author: king
"""

import requests

from json import JSONDecoder

http_url ="https://api-cn.faceplusplus.com/facepp/v3/search"

key ="QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"
secret ="YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"

data = {"api_key": key, "api_secret": secret,"faceset_token":"644b2aed41b3d619f4109e384e5982d0",
        "return_result_count":5}
filepath='16t.jpg'
files = {"image_file": open(filepath, "rb")}

response=requests.post(http_url, data=data,files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)
print(req_dict)


