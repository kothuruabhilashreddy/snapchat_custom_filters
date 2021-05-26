import cv2
import dlib
import urllib
import numpy as np
from imutils import face_utils, rotate_bound
from math import hypot
#nose_image=cv2.imread("C:\\Users\\ABHILASH REDDY\\Desktop\\Filters\\nose.png")
nose_gitimg=[

]
ear_gitimg=[

]
eyes_gitimg=[

]
spects_gitimg=[

]

req = urllib.request.urlopen('https://raw.githubusercontent.com/Horea94/Fruit-Images-Dataset/master/Test/Apple%20Braeburn/321_100.jpg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
nose_image = cv2.imdecode(arr, -1)
earimg=cv2.imread(r'C:\Users\ABHILASH REDDY\Desktop\Filters\opencv-facefilters-master\dog_ears.png')
class filter(object):
    
    def nose_filter(landmarks,frame1,val):

        top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        nose_width = int(hypot(left_nose[0] - right_nose[0],
                       left_nose[1] - right_nose[1]) * 1.7)
        nose_height = int(nose_width * 0.77)
        top_left_nose = (int(center_nose[0] - nose_width / 2),
                          int(center_nose[1] - nose_height / 2))
        bottom_right_nose = (int(center_nose[0] + nose_width / 2),
                   int(center_nose[1] + nose_height / 2))
        #input image
        req = urllib.request.urlopen(val)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        nose_image = cv2.imdecode(arr, -1)
        nose_pig = cv2.resize(nose_image, (nose_width, nose_height))
        nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
        _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)
        nose_area = frame1[top_left_nose[1]: top_left_nose[1] + nose_height,
                top_left_nose[0]: top_left_nose[0] + nose_width]
        nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
        final_nose = cv2.add(nose_area_no_nose, nose_pig)
        frame1[top_left_nose[1]: top_left_nose[1] + nose_height,
        top_left_nose[0]: top_left_nose[0] + nose_width] = final_nose
        return frame1


    def ear_filter(landmarks,frame1,val):
        left_forehead = (landmarks.part(20).x,landmarks.part(20).y)
        right_forehead = (landmarks.part(24).x,landmarks.part(24).y)
        center_forehead = (landmarks.part(28).x, landmarks.part(28).y)
        forehead_width = int(hypot(left_forehead[0]-right_forehead[0],left_forehead[1]-right_forehead[1])*3.5)
        forehead_height = int(forehead_width*0.4)
        max_x=frame1.shape[0]
        max_y=frame1.shape[1]
        top_left_ears_x=int(center_forehead[0]-forehead_width/2)
        top_left_ears_y=int(center_forehead[1]-forehead_height*2)
        if(top_left_ears_x<0):
            top_left_ears_x=0
        if(top_left_ears_y<0):
            top_left_ears_y=0
        top_left_ears = (top_left_ears_x,top_left_ears_y)
        # bottom_right_ears_x=int(center_forehead[0]+forehead_width/2)
        # bottom_right_ears_y=int(center_forehead[1]+forehead_height)
        bottom_right_ears_x=int(center_forehead[0])
        bottom_right_ears_y=int(center_forehead[1])
        if(bottom_right_ears_y>max_y):
            bottom_right_ears_y=max_y
        if(bottom_right_ears_x>max_x):
            bottom_right_ears_x=max_x
        bottom_right_ears = (bottom_right_ears_x,bottom_right_ears_y)
        #input image
        req = urllib.request.urlopen(val)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        earimg = cv2.imdecode(arr, -1)
        ears = cv2.resize(earimg,(forehead_width,forehead_height))
        ears_gray = cv2.cvtColor(ears,cv2.COLOR_BGR2GRAY)
        _, ears_mask = cv2.threshold(ears_gray,25,255,cv2.THRESH_BINARY_INV)
        ears_area = frame1[top_left_ears[1]:top_left_ears[1]+forehead_height,
                            top_left_ears[0]:top_left_ears[0]+forehead_width]
        
        ears_area_no_ears = cv2.bitwise_and(ears_area, ears_area, mask=ears_mask)
        final_ears = cv2.add(ears_area_no_ears,ears)
        frame1[top_left_ears[1]: top_left_ears[1]+forehead_height,
                         top_left_ears[0]:top_left_ears[0]+forehead_width] = final_ears
        return frame1

    
    def eye_filter(landmarks,frame1,val):
        left_eyes=(landmarks.part(37).x,landmarks.part(37).y)
        right_eyes=(landmarks.part(46).x,landmarks.part(46).y)
        center_eyes=(landmarks.part(29).x,landmarks.part(29).y)
        eyes_width=int(hypot(left_eyes[0]-right_eyes[0],left_eyes[1]-right_eyes[1])*1.5)
        eyes_height = int(eyes_width*0.3)
        max_x=frame1.shape[0]
        max_y=frame1.shape[1]
        top_left_eyes_x=int(center_eyes[0]-eyes_width/2)
        top_left_eyes_y=int(center_eyes[1]-eyes_height)
        if(top_left_eyes_x<0):
            top_left_eyes_x=0
        if(top_left_eyes_y<0):
            top_left_eyes_y=0
        top_left_eyes = (top_left_eyes_x,top_left_eyes_y)
        bottom_right_eyes_x=int(center_eyes[0]+eyes_width/2)
        bottom_right_eyes_y=int(center_eyes[1]+eyes_height)
        if(bottom_right_eyes_y>max_y):
            bottom_right_eyes_y=max_y
        if(bottom_right_eyes_x>max_x):
            bottom_right_eyes_x=max_x
        bottom_right_ears = (bottom_right_eyes_x,bottom_right_eyes_y)
        #input
        req = urllib.request.urlopen(val)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        eyesimg = cv2.imdecode(arr, -1)
        eyes = cv2.resize(eyesimg,(eyes_width,eyes_height))
        eyes_gray = cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY)
        _, eyes_mask = cv2.threshold(eyes_gray,25,255,cv2.THRESH_BINARY_INV)
        eyes_area = frame1[top_left_eyes[1]:top_left_eyes[1]+eyes_height,
                            top_left_eyes[0]:top_left_eyes[0]+eyes_width]
        
        eyes_area_no_eyes = cv2.bitwise_and(eyes_area, eyes_area, mask=eyes_mask)
        final_eyes = cv2.add(eyes_area_no_eyes,eyes)
        frame1[top_left_eyes[1]: top_left_eyes[1]+eyes_height,
                         top_left_eyes[0]:top_left_eyes[0]+eyes_width] = final_eyes
        return frame1


    def spects_filter(landmarks,frame1,val):
        left_spects=(landmarks.part(1).x,landmarks.part(1).y)
        right_spects=(landmarks.part(17).x,landmarks.part(17).y)
        center_spects=(landmarks.part(29).x,landmarks.part(29).y)
        spects_width=int(hypot(left_spects[0]-right_spects[0],left_spects[1]-right_spects[1])*6.9)
        spects_height = int(spects_width*0.3)
        max_x=frame1.shape[0]
        max_y=frame1.shape[1]
        top_left_spects_x=int(center_spects[0]-spects_width/2)
        top_left_spects_y=int(center_spects[1]-spects_height)
        if(top_left_spects_x<0):
            top_left_spects_x=0
        if(top_left_spects_y<0):
            top_left_spects_y=0
        top_left_spects = (top_left_spects_x,top_left_spects_y)
        bottom_right_spects_x=int(center_spects[0]+spects_width/2)
        bottom_right_spects_y=int(center_spects[1]+spects_height)
        if(bottom_right_spects_y>max_y):
            bottom_right_spects_y=max_y
        if(bottom_right_spects_x>max_x):
            bottom_right_spects_x=max_x
        bottom_right_ears = (bottom_right_spects_x,bottom_right_spects_y)
        #input
        req = urllib.request.urlopen(val)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        spectsimg = cv2.imdecode(arr, -1)
        spects = cv2.resize(spectsimg,(spects_width,spects_height))
        spects_gray = cv2.cvtColor(spects,cv2.COLOR_BGR2GRAY)
        _, spects_mask = cv2.threshold(spects_gray,25,255,cv2.THRESH_BINARY_INV)
        spects_area = frame1[top_left_spects[1]:top_left_spects[1]+spects_height,
                            top_left_spects[0]:top_left_spects[0]+spects_width]
        
        eyes_area_no_eyes = cv2.bitwise_and(spects_area, spects_area, mask=spects_mask)
        final_spects = cv2.add(eyes_area_no_eyes,spects)
        frame1[top_left_spects[1]: top_left_spects[1]+spects_height,
                         top_left_spects[0]:top_left_spects[0]+spects_width] = final_spects
        return frame1


        
