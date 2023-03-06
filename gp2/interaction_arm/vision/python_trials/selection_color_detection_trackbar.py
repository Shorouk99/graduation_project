# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np


img = cv2.imread('elev3.jpeg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow('tuning')

def nothing(val):
	pass

cv2.createTrackbar('h_low', 'tuning', 0, 250, nothing)
cv2.createTrackbar('h_high', 'tuning', 0, 250, nothing)
cv2.createTrackbar('s_low', 'tuning', 0, 250, nothing)
cv2.createTrackbar('s_high', 'tuning', 0, 250, nothing)
cv2.createTrackbar('v_low', 'tuning', 0, 250, nothing)
cv2.createTrackbar('v_high', 'tuning', 0, 250, nothing)

while(1):

	h_up = int(cv2.getTrackbarPos('h_high','tuning'))
	s_up = int(cv2.getTrackbarPos('s_high','tuning'))
	v_up = int(cv2.getTrackbarPos('v_high','tuning'))

	h_low = int(cv2.getTrackbarPos('h_low','tuning'))
	s_low = int(cv2.getTrackbarPos('s_low','tuning'))
	v_low = int(cv2.getTrackbarPos('v_low','tuning'))

	lower_green = np.array([h_low,s_low,v_low])
	upper_green = np.array([h_up,s_up,v_up])

	mask = cv2.inRange(hsv, lower_green, upper_green )

	res = cv2.bitwise_and(img,img, mask= mask)
	cv2.imshow('res',res)
	cv2.waitKey(1)

