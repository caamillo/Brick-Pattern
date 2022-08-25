from PIL import Image, ImageDraw
import numpy as np
import cv2

imgW, imgH = 1920, 1080

print('Image size:', imgW, 'x', imgH)

img = Image.new(
    'RGB', # Mode
    (imgW, imgH), # Size
    'white'
)

with open('pattern.png') as pattern:
    pass

# OpenCV Show

cvImage = np.array(img)
cvImage = cvImage[:, :, ::-1].copy() # rgb -> bgr

cv2.imshow('image', cvImage)
cv2.waitKey(0)