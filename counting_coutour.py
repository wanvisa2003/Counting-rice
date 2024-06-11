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

plt.subplot(1,2,1),plt.imshow(thresh)
plt.title("Edge Detection"), plt.xticks([]), plt.yticks([])
for(i, c) in enumerate(sorted_contours):
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(image, text=str(i + 1), org=(cx, cy),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # cv2.putText(image, text=str(i + 1), org=(cx, cy),
    #             fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 0),
    #             thinkness=2, lineType=cv2.LINE_AA)
    print(i)
plt.subplot(1, 2, 2),plt.imshow(image)
plt.title('Couting'), plt.xticks([]), plt.yticks([])
plt.show()

