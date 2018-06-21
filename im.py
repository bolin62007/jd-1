from cv2 import *
from skimage import measure,draw
import numpy as np



if __name__ == '__main__':
#    im=imread(r"C:\Users\liupe\Pictures\1.bmp")
    im=imread(r"d:\1.bmp",0)
    imshow("haha",im)
    
    print(im)
    (b, g, r) = split(im)  
    
    edge_g = Canny(g, 0, 0)
    imshow('edgeg', edge_g) 
    edge_b = Canny(b, 0, 0) 
    imshow('edgeb', edge_b) 
    edge_r = Canny(r, 0, 0) 
    imshow('edger', edge_r) 
    
    im1=addWeighted(edge_g, 0.5,edge_b,0.5,0)
    im1=addWeighted(edge_r, 0.5,im1     ,0.5,0)
#    imshow('int',im1)
    im2=edge_b+edge_g+edge_r
#    im3=cvtColor(im2,COLOR_BGR2GRAY)
    im4=threshold(im2,127,255,THRESH_BINARY)
    imshow('int',im2)
    print(im4)
    
#    contours = measure.find_contours(im2, 0.5)
#    print(contours)
 #   for n, contour in enumerate(contours):
        
        
    
    waitKey(0)
    destroyAllWindows()
    
