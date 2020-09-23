import cv2

# -----------------------read input image--------------
img=cv2.imread("input.jpg")
# convert into gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#read mask image
mask=cv2.imread("mask.png",0)
#resize mask
resize_mask=cv2.resize(mask, (gray.shape[1],gray.shape[0]), interpolation = cv2.INTER_AREA)


img2_fg = cv2.bitwise_or(img,img,mask = resize_mask)
final_image=img2_fg.copy()
ret, thresh = cv2.threshold(cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY), 0, 10, cv2.THRESH_BINARY)
final_image[thresh == 0] = (0,0,255)

cv2.imwrite("output.jpg",final_image)