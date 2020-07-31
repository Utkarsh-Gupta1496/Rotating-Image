"""
Created on Wed Dec  4 18:12:14 2019

@author: utkarsh
"""

import numpy as np 
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('.data/peppersgrey.jpg')
img = img[:,:,0]
img2=np.zeros((np.shape(img)[0]+1,np.shape(img)[1]+1)) 
img2[1:np.shape(img)[0]+1,1:np.shape(img)[1]+1] = img


s_row=img.shape[0]
s_col=img.shape[1]

s_row = int(s_row)  //2
s_col = int(s_col)  //2

x, y = np.mgrid[-s_row:s_row+1, -s_col:s_col+1]

# Rotate Image by angle(degrees) specified by theta.
theta=50
theta=theta*np.pi/180


x_new=((np.cos(theta)*(x))-(np.sin(theta)*(y)))
y_new=((np.sin(theta)*(x))+(np.cos(theta)*(y)))

x_new=np.asarray(x_new,np.int64)
y_new=np.asarray(y_new,np.int64)

x_new=x_new+x_new.max()
y_new=y_new+y_new.max()

empty=np.zeros((x_new.max()+1,y_new.max()+1))

for i in range(513):
    for j in range(513):
        empty[x_new[i,j],y_new[i,j]]=img2[i,j]

def bilinear(new_img):
    N = new_img.shape[0]
    out_img = np.zeros([N,N])

    for i in range(N):
        for j in range(N-1):
            if(new_img[i,j] == 0):
                new_img[i,j] = 0.5*(new_img[i,j-1]+new_img[i,j+1])

    for i in range(N):
        for j in range(N-1):
            if(new_img[j,i] == 0):
                out_img[j,i] = 0.5*(new_img[j-1,i] + new_img[j+1,i])
            else:
                out_img[j,i] = new_img[j,i]
    return out_img

a=bilinear(empty)

plt.imshow(a,cmap='gray')
