from PIL import Image, ImageDraw
import numpy as np
import cv2

outputW, outputH = 1920, 1080
outputDistanceX, OutputDistanceY = 5, 5

print('Output size:', outputW, 'x', outputH)

output = Image.new(
    'RGB', # Mode
    (outputW, outputH), # Size
    'white'
)

pattern = Image.open('pattern.png')
patternW, patternH = pattern.size
patternPixels = pattern.load()

for y in range(patternH):
    for x in range(patternW):
        print(patternPixels[x, y])

# OpenCV Show

cvImage = np.array(output)
cvImage = cvImage[:, :, ::-1].copy() # rgb -> bgr

cv2.imshow('image', cvImage)
cv2.waitKey(0)