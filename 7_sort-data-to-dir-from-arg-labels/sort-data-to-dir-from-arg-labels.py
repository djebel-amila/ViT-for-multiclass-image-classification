# This Python script will sort files into new directories from arguments passed in the command prompt. They have to match the labels contained in the second columns of the "labels.csv" file. 
# /!\ if an image has more than one label the script will crash and stop at this point. 
# /!\ if an image has no label it won’t be placed in any folder. 
# use: In terminal, run program followed by the categories present in the second columns of the "labels.csv" file, i.e.: 
# $python sort-data-to-dir-from-arg-labels.py in out none
# will sort the files and place them in the corresponding subfolders (.in/, .out/, .none/). 

import csv
import os
import pathlib
import sys 

# remove the first sys.argv (the program name) to keep only arguments passed after that
sys.argv.remove(sys.argv[0])

# iterate over arguments list
for x in sys.argv:
  with open('./labels.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['file','state'], delimiter=',')
    # skip header
    next(reader)
    for r in reader:
        existGDBPath = pathlib.Path('data/'+r['file'])

        targetFolder = existGDBPath.parent

        folder = str(targetFolder) + "/" + x
        inExist = os.path.exists(folder)
        if not inExist:
            os.makedirs(folder)
        if str(r['state']).upper() == str(x).upper():
            pathlib.Path('data/'+r['file']).rename(str(targetFolder) + '/' + x + '/' + str(os.path.basename(r['file'])))