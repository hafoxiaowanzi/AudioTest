#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/14 16:39 
# @Author : wanxin
# @File : how_to_use_camera.py 
# @Software: PyCharm

import cv2
import dlib

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture(0)

cap.set(3, 480)

print(cap.isOpened())

while cap.isOpened():
    ret_flag,imag_camera = cap.read()

    faces = detector(imag_camera, 1)
    print("人脸数据 / Face in all：", len(faces))

    for i, d in enumerate(faces):
        print("第", i + 1, "个人脸的矩形框坐标:", "left:", d.left(), "right:", d.right(), "top:", d.top(), "bottom:", d.bottom())
        cv2.rectangle(imag_camera, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255), 2)
    cv2.imshow("Camera", imag_camera)
    k = cv2.waitKey(1)

    if k == ord('s'):
        cv2.imwrite("faces_2.jpg", imag_camera)

    if k ==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


