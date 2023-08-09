# This Python script will browse through all directories contained in the "data" directory. 
# It will randomly extract a specified amount (percentage) of files among them. 
# It will create strict copies and place them in a new directory named "random-data". 
# use: In terminal, run program followed by the desired ratio/amount (%) of random files selected, i.e.: 
# python extract-random-files.py 0.05
# will randomly select 5% of the total amount of files in the subfolders and copy-paste them in the "random-data" folder. 

import os
import math
import random
import shutil

import sys
folder = "data"
factor = float(sys.argv[1])

#directories = os.listdir('./data');
directories = os.listdir('./' + folder);

targetDir = './random-files';

targetDirExist = os.path.exists(targetDir)

if not targetDirExist:
    os.makedirs(targetDir)

for i in directories:
    currentSelection = []
    if os.path.isdir(folder + '/' + i):
        files = os.listdir(folder + '/' + i)
        nbFileToTake = len(files) * factor
        randomFiles = random.sample(files, math.ceil(nbFileToTake));
        for j in randomFiles:
            filename = folder + '/' + i + '/' + j;
            shutil.copyfile(filename, str(targetDir) + '/' + j);

print("browsed through '", folder,"'’s subdirectories and extracted", factor * 100, "% of their content")