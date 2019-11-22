import cv2
import os



count = 1
IMG_COL = 50
IMG_ROW = 100

while (count < 1093):
    img = cv2.imread("neg/"+str(count)+".jpg")
    # Resize
    border_v = 0
    border_h = 0
    if (IMG_COL / IMG_ROW) >= (img.shape[0] / img.shape[1]):
        border_v = int((((IMG_COL / IMG_ROW) * img.shape[1]) - img.shape[0]) / 2)
    else:
        border_h = int((((IMG_ROW / IMG_COL) * img.shape[0]) - img.shape[1]) / 2)
    img = cv2.copyMakeBorder(img, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, 0)
    img = cv2.resize(img, (IMG_ROW, IMG_COL))
    cv2.imwrite("neg/"+str(count)+"new1.jpg",img)
    count += 1