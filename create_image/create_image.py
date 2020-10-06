import cv2
import numpy as np

# -----------------------read input image--------------
img=cv2.imread("input.jpg")
# convert into gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#read mask image
mask=cv2.imread("mask.png")

#resize mask
resize_mask=cv2.resize(mask,(gray.shape[1],gray.shape[0]), interpolation = cv2.INTER_AREA)


# dst = cv2.addWeighted(img, 0.8,resize_mask, 0.05, 0)
mask_gray=cv2.cvtColor(resize_mask,cv2.COLOR_BGR2GRAY)

#erode
kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(mask_gray,kernel,iterations = 2)

img2_fg = cv2.bitwise_or(img,img,mask = erode)
final_image=img2_fg.copy()

ret, thresh = cv2.threshold(cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY), 0, 10, cv2.THRESH_BINARY)
final_image[thresh == 0] = (0,0,255)

#blank red background image
full_layer = np.full((5170, 4480,3), (0,0,255), np.uint8)
cnts = cv2.findContours(cv2.cvtColor(resize_mask, cv2.COLOR_BGR2GRAY), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

# Find bounding box and extract ROI
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    ROI = final_image[y:y+h, x:x+w]
    break

h, w,ly = ROI.shape
# print(h,w,ly)

hh, ww,ly = full_layer.shape
# print(hh,ww,ly)

yoff = round((hh-h)/2)
xoff = round((ww-w)/2)
# print(yoff,xoff)

#overlay image at center
result = full_layer.copy()
result[yoff:yoff+h, xoff:xoff+w] = ROI

#output
cv2.imwrite("output.jpg",result)