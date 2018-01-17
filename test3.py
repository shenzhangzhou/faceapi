# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:17:28 2018

@author: king
"""
#face++测试 success
import cv2
import requests
from json import JSONDecoder
#显示原图
img = cv2.imread("16t.jpg")
cv2.namedWindow("original")
cv2.imshow("original", img)

#调用接口API
http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key = "QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"
secret = "YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"
filepath = "16t.jpg"
#调用参数  详情参见Face++ 文档  这里可选参数只选择 年纪 性别 
data = {"api_key": key, "api_secret": secret, "return_landmark": "1","return_attributes":"gender,age"}
files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)
#返回的json
print(req_dict)

mydict = eval(str(req_dict))

face = mydict.get('faces')

  
faceNum = len(face)
print("识别到了%d个人脸"%(faceNum))
time=mydict.get('time_used')    #请求时间
print(time,'ms')

#显示脸部识别  并且输出年纪 性别

for i in range(faceNum):
    face_rectangle = face[i]['face_rectangle']
    face_token=face[i]['face_token']
    
    width =  face_rectangle['width']
    top =  face_rectangle['top']
    left =  face_rectangle['left']
    height =  face_rectangle['height']
    start = (left, top)
    end = (left+width, top+height)
    color = (55,255,155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)
    
    att=face[i]['attributes']
    age=att['age']['value']
    gender=att['gender']['value']
    print('编号',i,' ','年纪：',age,'性别：',gender,left,face_token)
    
    
cv2.namedWindow("now")
while(1):
    cv2.imshow('now',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()


