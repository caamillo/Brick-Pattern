from PIL import Image, ImageDraw
import numpy as np
import cv2

# Output

outputW, outputH = 1920, 1080
outputDistanceX, OutputDistanceY = 5, 5

print('Output size:', outputW, 'x', outputH)

output = Image.new(
    'RGB', # Mode
    (outputW, outputH), # Size
    'black' # Background Color
)

# Pattern

pattern = Image.open('pattern.png')
patternW, patternH = pattern.size
patternPixels = pattern.load()

# Pattern Replacing Loop

for y in range(outputH):
    for x in range(outputW):
        if y < patternH and x < patternW and patternPixels[x, y][3] != 0:
            output.putpixel((x, y), patternPixels[x, y])

# OpenCV Show

cvImage = np.array(output)
cvImage = cvImage[:, :, ::-1].copy() # rgb -> bgr

cv2.imshow('image', cvImage)
cv2.waitKey(0)