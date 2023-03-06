import cv2
import numpy as np
import matplotlib.pyplot as plt
from selection_color_detection import detect_selected
from button_isolation import isolate_buttons

img = cv2.imread('elev3.jpeg', cv2.IMREAD_COLOR)

buttons = isolate_buttons(img)
if len(buttons) > 0:
	for button in buttons:
		print(button.shape)
		res, selected = detect_selected(button)
		print("selected", selected)
		plt.imshow(button)
		plt.show() 