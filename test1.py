# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:09:34 2018

@author: king
"""
# Request 问题  尚未解决
import cv2
import urllib
import time

#读取原图，并显示
img = cv2.imread("2.1.jpg")
cv2.namedWindow("原图")
cv2.imshow("原图", img)

#URL
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect' 
#用户信息
key = "QjAJnCFEJgJTUg6WcEFcnDGL0N5IyQN8"    
secret = "YoqJM4wDR0GJUeJx3c8rHrqfP1YGzhzS"
#图片存储路径
filepath = r"./2.1.jpg"

#这后面的都是给的示例代码，调用API接口
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)

fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)

c=str(data)
http_body='\r\n'.join(c)
#buld http request
req=urllib.request.Request(http_url)

#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add.data(http_body)
try:
    #req.add_header('Referer','http://remotserver.com/')
    #post data to server
    resp = urllib.request.urlopen(req, timeout=5)
    #get response
    qrcont=resp.read()
    print(qrcont)        #打印出得到的结果

except urllib.request.HTTPError as e:
    print(e.read())

#进过测试前面的程序会返回一个字典，其中指出了人脸所在的矩形的位置和大小等，所以直接进行标注


# print type(resp)