#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2019/5/14 17:37 
# @Author : wanxin
# @File : face_from_camera.py 
# @Software: PyCharm


import dlib
import cv2
import time
import os

path_screenshots ="facerecognition/imgs/screenshots/"

isExists = os.path.exists(path_screenshots)

# 判断结果
if not isExists:
    os.makedirs(path_screenshots)

detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor('data/dlib/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

cap.set(3, 960)

ss_cnt = 0

while cap.isOpened():
    flag, img_rd = cap.read()

    k = cv2.waitKey(1)

    img_gray = cv2.cvtColor(img_rd,cv2.COLOR_RGB2GRAY)

    faces = detector(img_gray, 0)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if k == ord('q'):
        break
    else:
        if len(faces) != 0:
            faces_start_width =0

            for face in faces:

                cv2.rectangle(img_rd,tuple([face.left(),face.top()]),tuple([face.right(),face.bottom()]),(0,255,255),2)

                height = face.bottom() - face.top()
                width = face.right() - face.left()

                if(face.bottom() < 480 ) and (face.right() < 640) and ((face.top() + height) < 480) and ((face.left() + width) < 640 ):
                    for i in range(height):
                        for j in range(width):
                            img_rd[i][faces_start_width+j] = img_rd[face.top()+i][face.left() + j]

                faces_start_width += width

            cv2.putText(img_rd,"Face in all:"+str(len(faces)),(20,350),font,0.8,(0,0,0),1,cv2.LINE_AA)

        else:

            cv2.putText(img_rd,"no face",(20,350),font,0.8,(0,0,0),1,cv2.LINE_AA)

        img_rd = cv2.putText(img_rd,"Press 's':Scress shot",(20,400),font,0.8,(255,255,255),1,cv2.LINE_AA)
        img_rd = cv2.putText(img_rd,"Press 'Q':Quit",(20,450),font,0.8,(255,255,255),1,cv2.LINE_AA)

    if k ==ord('s'):
        ss_cnt += 1
        print(path_screenshots + "screenshot" +  "_" + str(ss_cnt) + "_" + time.strftime("%Y-%m-%d-%H-5M-%S",time.localtime())+".jpg")
        cv2.imwrite(path_screenshots + "screenshot" +  "_" + str(ss_cnt) + "_" + time.strftime("%Y-%m-%d-%H-5M-%S",time.localtime())+".jpg",img_rd)
    cv2.namedWindow("Camera", 1)
    cv2.imshow("Camera", img_rd)


cap.release()
cv2.destroyAllWindows()



