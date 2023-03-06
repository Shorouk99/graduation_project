import cv2
import numpy as np
import matplotlib.pyplot as plt
# from selection_color_detection import detect_selected

def isolate_buttons(img, gaussian_size=5, dp=1, min_dist=20, param1=100, param2=70, r_min=10, r_max=100):
	isolated_buttons = []

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray_blurred = cv2.blur(gray, (gaussian_size, gaussian_size))
	detected_circles = cv2.HoughCircles(gray_blurred,
				cv2.HOUGH_GRADIENT, dp, min_dist, param1,
			param2, minRadius=r_min, maxRadius=r_max)

	if detected_circles is not None:

		# Convert the circle parameters a, b and r to integers.
		detected_circles = np.uint16(np.around(detected_circles))

		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]

			# print('center = ', (a,b), 'radius = ', r)
			# print ("img shape", img.shape)
			# Draw the circumference of the circle.
			# cv2.circle(img, (a, b), r, (0, 255, 0), 2)

			# # Draw a small circle (of radius 1) to show the center.
			# cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

			low_row_bound = b-r
			if low_row_bound < 0:
				low_row_bound = 0

			high_row_bound = b+r
			if high_row_bound > img.shape[0]:
				high_row_bound = img.shape[0]

			low_col_bound = a-r
			if low_col_bound < 0:
				low_col_bound = 0

			high_col_bound = a+r
			if high_col_bound > img.shape[1]:
				high_col_bound = img.shape[1]


			cropped_img = img[low_row_bound:high_row_bound, low_col_bound:high_col_bound]
			isolated_buttons.append(cropped_img)

	return isolated_buttons

# img = cv2.imread('elev4.jpeg', cv2.IMREAD_COLOR)
# buttons = isolate_buttons(img)
# if len(buttons) > 0:
# 	for button in buttons:
# 		print (button.shape)
# 		plt.imshow(button)
# 		plt.show() 
