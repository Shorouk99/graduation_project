import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image.
img = cv2.imread('elev4.jpeg', cv2.IMREAD_COLOR)

# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (5, 5))

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred,
				cv2.HOUGH_GRADIENT, 1, 20, param1 = 100,
			param2 = 70, minRadius = 10, maxRadius = 100)

# Draw circles that are detected.
if detected_circles is not None:

	# Convert the circle parameters a, b and r to integers.
	detected_circles = np.uint16(np.around(detected_circles))

	for pt in detected_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]

		print('center = ', (a,b), 'radius = ', r)
		print ("img shape", img.shape)
		# Draw the circumference of the circle.
		cv2.circle(img, (a, b), r, (0, 255, 0), 2)

		# Draw a small circle (of radius 1) to show the center.
		cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

		low_row_bound = b-r
		if low_row_bound < 0:
			low_row_bound = 0

		high_row_bound = b+r
		if high_row_bound > img.shape[0]:
			high_row_bound = img.shape[0]

		# print("low row", low_row_bound)
		# print("high row", high_row_bound)

		low_col_bound = a-r
		if low_col_bound < 0:
			low_col_bound = 0

		high_col_bound = a+r
		if high_col_bound > img.shape[1]:
			high_col_bound = img.shape[1]

		# print("high_col", high_col_bound)
		# print("low_col", low_col_bound)


		cropped_img = img[low_row_bound:high_row_bound, low_col_bound:high_col_bound]
		print("\n",cropped_img.shape)
		plt.imshow(cropped_img)
		plt.show()
		
plt.imshow(img)
plt.show()
