#coding=utf-8  
import cv2  
import numpy as np    
  
img = cv2.imread("D:/1.bmp", 0)  
cv2.imshow("1",img)  
img = cv2.GaussianBlur(img,(3,3),0) 
cv2.imshow("2",img) 
canny = cv2.Canny(img, 50,150)  
  
cv2.imshow('Canny', canny)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  