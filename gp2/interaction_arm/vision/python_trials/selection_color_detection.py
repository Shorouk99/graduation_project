# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np
import matplotlib.pyplot as plt




def detect_selected(img, h_high=74, h_low=47, s_high=250, s_low=33, v_high=250, v_low=0):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([h_low,s_low,v_low])
    upper_green = np.array([h_high, s_high, v_high])

    mask = cv2.inRange(hsv, lower_green, upper_green )
    pixels = cv2.countNonZero(mask)
    if pixels > 20:
        selected = True
        print("green exist")
    else: 
        selected = False
        print("not found")

    res = cv2.bitwise_and(img,img, mask= mask)

    return res, selected

# img = cv2.imread('elev10.jpeg', cv2.IMREAD_COLOR)
# res, selected = detect_selected(img)
# print("is selected? ", selected)
# plt.imshow(res)
# plt.show()