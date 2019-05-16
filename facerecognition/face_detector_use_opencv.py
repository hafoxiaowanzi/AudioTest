#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/14 16:47 
# @Author : wanxin
# @File : face_detector_use_opencv.py 
# @Software: PyCharm

import cv2
import dlib

detector = dlib.get_frontal_face_detector()


img = cv2.imread("imgs/faces_2.jpg")
# cv2.imshow("1",img)

faces = detector(img, 1)
print("人脸数据 / Face in all：", len(faces))

for i, d in enumerate(faces):
    print("第",i+1,"个人脸的矩形框坐标:","left:",d.left(),"right:",d.right(),"top:",d.top(),"bottom:",d.bottom())
    cv2.rectangle(img,tuple([d.left(),d.top()]),tuple([d.right(),d.bottom()]),(0,255,255),2)

cv2.namedWindow("img",2)
cv2.imshow("img",img)
cv2.waitKey(0)



