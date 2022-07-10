import matplotlib.pyplot as plt
import numpy as np
import cv2
# read image
PATH = 'lena.jpg'
noisy_image = cv2.imread(PATH)
cv2.imshow('Original' , noisy_image)
kernel = np.ones((5,5),np.float32)/25
conImage = cv2.filter2D(noisy_image,-1,kernel)
cv2.imshow('FIltered Image', conImage)
colors = ['green', 'blue', 'lime']


cv2.waitKey(0)