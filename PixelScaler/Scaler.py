#Scaler
#Created By: TearlessCape914


#Import Modules
import cv2
import os


#Settings
cur_folder = '\\'.join(__file__.split('\\')[:-1])
scale = 2


#Main Loop
for img in os.listdir(os.path.join(cur_folder,'Img-In')):
    image = cv2.imread(os.path.join(cur_folder,'Img-In',img), cv2.IMREAD_UNCHANGED)
    new_image = cv2.resize(image,tuple([int(image.shape[0]*scale),int(image.shape[1]*scale)]),interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(cur_folder,'Img-Out',img.split('\\')[-1]),new_image)