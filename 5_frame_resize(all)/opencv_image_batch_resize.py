# This Python script will create resized copies of all the images contained in a directory and its subdirectories to the specified dimensions (x, y). 
#*It will also ignore the invisible files that begin with "."
# It will place the duplicated and resized image files in a new directory named after the original directory + "-resized" + the specified dimensions. 
# use: In terminal, run program followed by the path to directory, i.e.: 
# $python opencv_image_batch_resize.py 224 224
# will duplicate and resize all the image files in the "data" folder and place them in a new folder named "data-resized_224_224". 

import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import csv
import sys 

dimensionA = int(sys.argv[1])
dimensionB = int(sys.argv[2])

filePath = './data'
directories = os.listdir(filePath);
newDir = str(filePath) + "-resized"
print(newDir)
for i in directories:
    if os.path.isdir('./data/' + i):
        files = os.listdir('./data/' + i)
        for j in files:
            if (j.startswith('.')):
                print(j)
            else:
                filename = 'data/' + i + '/' + j
                filename_only = str(filename.split("/")[2])
                src = cv.imread(filename, cv.IMREAD_UNCHANGED)
                # img2 = img.copy()
                # resize image
                dsize = (dimensionA, dimensionB)
                output = cv.resize(src, dsize, interpolation = cv.INTER_AREA)
                # Check whether the specified path exists or not
                isExist = os.path.exists(newDir+"_"+str(dimensionA)+"_"+str(dimensionB))
                if not isExist:
                  # Create a new directory because it does not exist
                  os.makedirs(newDir+"_"+str(dimensionA)+"_"+str(dimensionB))
                cv.imwrite(f"{newDir}_{dimensionA}_{dimensionB}/{filename_only}",output) 
