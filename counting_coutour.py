import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path  = 'rrice.jpg'
image = cv2.imread(image_path)
original_image = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)