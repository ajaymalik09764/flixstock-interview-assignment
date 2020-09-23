import cv2
import os, fnmatch

# ---------------------querry image-----------------------
img=cv2.imread("image/querry.jpg")        

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize_img=cv2.resize(gray, (240, 360 ),interpolation = cv2.INTER_NEAREST)
  
listOfFiles = os.listdir('dataBase-20200922T095631Z-001/database/')
pattern = "*.jpg"
images_name=[]
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
           images_name.append(entry)



#---------------------------matching result---------------------------
matching_result=[]


for name in images_name:
	#read image
	img2=cv2.imread("dataBase-20200922T095631Z-001/database/"+name)
	img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	resize_img2=cv2.resize(img2, (240, 360 ),interpolation = cv2.INTER_NEAREST)
	
	#----------------match feature with orb
	sift = cv2.ORB_create()	
	keypoints_1, descriptors_1 = sift.detectAndCompute(resize_img,None)
	keypoints_2, descriptors_2 = sift.detectAndCompute(resize_img2,None)
	
	bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
	
	matches = bf.match(descriptors_1,descriptors_2)
	matching_result.append(len(matches))  

#--------------------most similar image name--------------------------------          

print(images_name[matching_result.index(max(matching_result))])















