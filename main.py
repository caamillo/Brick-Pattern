from PIL import Image, ImageDraw
from math import floor
import numpy as np
import cv2

# Output

outputW, outputH = 1280, 720
outputDistanceX, OutputDistanceY = 100, 100
outputBackgroundColor = (0, 0, 0)
outputDensity = 1

print('Output size:', outputW, 'x', outputH)

output = Image.new(
    'RGB', # Mode
    (outputW, outputH), # Size
    'black' # Background Color
)

# Pattern

def deleteTransparency(im):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, outputBackgroundColor + (255,))
        bg.paste(im, mask=alpha)
        return bg
    else:
        return im

pattern = deleteTransparency(Image.open('pattern.png'))
patternW, patternH = pattern.size
patternPixels = pattern.load()

# Pattern Replacing Loop

# Calculating Tiles

grouptiles = [
    [],
    []
]

for i in range(2):
    idx = 0
    idx += patternW
    if i:
        idx *= 2
    while True:
        if idx < outputW:
            print(i, patternW, idx - patternW, idx)
            grouptiles[i].append((idx - patternW, idx))
            idx += (outputDistanceX + patternW) * outputDensity
        else:
            break

print(grouptiles)

y = 0
choicePattern = 0

while True:
    if y < outputH:
        tiles = grouptiles[choicePattern]
        for x, x2 in tiles:
            output.paste(pattern, (x, y))
        if not choicePattern:
            choicePattern += 1
        else:
            choicePattern -= 1
        y += (patternH + OutputDistanceY)
    else:
        break

# OpenCV Show

cvImage = np.array(output)
cvImage = cvImage[:, :, ::-1].copy() # rgb -> bgr

cv2.imshow('brick pattern', cvImage)
cv2.waitKey(0)