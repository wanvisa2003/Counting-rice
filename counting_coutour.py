import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path  = 'rrice.jpg'
image = cv2.imread(image_path)
original_image = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernal = np.ones((10, 10), np.uint8)
thresh = cv2.erode(thresh, kernal, iterations = 1)
thresh = cv2.dilate(thresh, kernal, iterations = 1)
kernal = np.ones((5,5), np.uint8)
thresh =  cv2.erode(thresh, kernal, iterations = 1)

contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sorted_contours = sorted(contour, key=cv2.contourArea, reverse=False)
