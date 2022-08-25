from PIL import Image, ImageDraw
import numpy as np
import cv2

# Output

outputW, outputH = 1920, 1080
outputDistanceX, OutputDistanceY = 5, 5
outputBackgroundColor = (0, 0, 0)

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

def deleteTransparency(im):
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, outputBackgroundColor + (255,))
        bg.paste(im, mask=alpha)
        return bg
    else:
        return im

"""
for y in range(outputH):
    for x in range(outputW):
        if y < patternH and x < patternW and patternPixels[x, y][3] != 0:
            output.putpixel((x, y), patternPixels[x, y])
"""

output.paste(deleteTransparency(pattern), (300, 300))

# OpenCV Show

cvImage = np.array(output)
cvImage = cvImage[:, :, ::-1].copy() # rgb -> bgr

cv2.imshow('image', cvImage)
cv2.waitKey(0)