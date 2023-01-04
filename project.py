import cv2 
import cvlib as cv
import numpy as np
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
import matplotlib.pyplot as plt
import requests


#membaca gambar 
img_as_rgb = cv2.imread('WhatsApp_Image_2022-12-18_at_21.28.24-removebg-preview (2).png')




#function untuk menunjukkan Gambar
def showimage(gambar):
    cv2.imshow('Projects UAS', gambar)
    cv2.waitKey(0)
    cv2.destroyAllWindows('Projects UAS')
    
# showimage(img_as_rgb)



# Mengubah format warna gambar dari RGB menjadi GrayScale
img_as_gray_scale = cv2.cvtColor(img_as_rgb, cv2.COLOR_RGB2GRAY)
showimage(img_as_gray_scale)

# Thresholding gambar dari gray scale menjadi warna putih dan hitam.
# Agar kita berfokus pada objeknya kita ubah warna background menjadi warna hitam, sedangkan warna objek putih
_, th1 = cv2.threshold(img_as_gray_scale, 220, 255, cv2.THRESH_BINARY_INV)


# function untuk membuat mengisi lubang pada object yang memiliki lubang
def fillhole(gambar):
    h, w = gambar.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    imfloodfill = gambar.copy()
    cv2.floodFill(imfloodfill, mask, (0,0), 255);
    imfloodfillinv = cv2.bitwise_not(imfloodfill)
    imout = th1 | imfloodfillinv
    return imout

imout = fillhole(th1)


# showimage(imout)

contours , hierarchy = cv2.findContours(imout ,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_as_rgb,contours, -1, (0,255,0))
# cv2.imshow('Img', img_as_rbg)
# cv2.imshow('Imout', imout)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
jumlah = str(len(contours))
print("jumlah: ", jumlah)

# box = cv2.rectangle()

fonts = cv2.FONT_HERSHEY_COMPLEX
color_mur = (75, 86, 210)
color_baut = (67, 154, 151)
font_thicknes = 2;
font_scale = 1;

# Mur = cv2.putText(img_as_rgb,'Mur/Nut',coords,fonts,font_scale,color_mur,font_thicknes)
# Baut = cv2.putText(img_as_rgb,'Baut/Bold',coords,fonts,font_scale,color_baut,font_thicknes)


# def findMetric(contours):
#     area = cv2.contourArea(contours[i])
#     perimeter = cv2.arcLength(contours[i], True)
#     metric = (4*np.pi*area) / (perimeter**2)
#     return metric
    
    
for i in range(int(jumlah)):
    
    area = cv2.contourArea(contours[i])
    perimeter = cv2.arcLength(contours[i], True)
    print('Nilai area:' , area)
    print('Nilai perimeter:' , perimeter)
    metric = (4*np.pi*area) / (perimeter**2)
    x,y,w,h = cv2.boundingRect(contours[i])
    print(x,y,w,h)
    x_mid = int(x + w/4)
    y_mid = int(y + h/2)
    coords = (x_mid,y_mid)
    print('Nilai Metric : ', metric)
    #Control flow untuk membandingkan antar mur dengan baut
    if metric > 0.7:
        #Creatting Boxes dan text around objeck
        cv2.rectangle(img_as_rgb,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.putText(img_as_rgb,'Mur/Nut',coords,fonts,font_scale,color_baut,font_thicknes)
    else:
        cv2.rectangle(img_as_rgb,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.putText(img_as_rgb,'Baut/Bold',coords,fonts,font_scale,color_mur,3)
        
# showimage(img_as_rgb)
        
        


#Creatting Boxes dan text around objeck 

