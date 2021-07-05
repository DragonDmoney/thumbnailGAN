# import cv2
#
# import PIL
# import os
# import os.path
# from PIL import Image
#
# savePath = r'./data/pewdsThumbnailsScaled(320x180)'
# f = r'./data/pewdsThumbnails'
#
# for file in os.listdir(f):
#     f_img = f+"/"+file
#     img = Image.open(f_img)
#     img = img.resize((320,180))
#     img.save(savePath+"/"+file)

import cv2

import PIL
import os
import os.path
from PIL import Image

savePath = r'./data/pewdsThumbnailsScaledSquareSmall'
f = r'.\data\pewdsThumbnails'

count = 0

print("wtf")
for file in os.listdir(f):
    count += 1
    print(file, count)
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((96,96))
    img.save(savePath+"/"+file)
