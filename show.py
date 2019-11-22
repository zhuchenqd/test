import cv2

path = '/user/chenzhu1/Download/workspace/opencv_workspace/neg'

image = cv2.imread('2356.jpg', 0)
cv2.imshow("window",image)
cv2.waitKey(0)