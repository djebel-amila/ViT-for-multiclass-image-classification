# sort files back into folders

import os
import csv
import sys 

arg = sys.argv[0]

filePath = './data'

directories = os.listdir(filePath);


with open("labels.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["filename", "targetFolder"])
    for i in directories:
        label = [i][0].split("-")
        newLine = i,label[0]
        csv_writer.writerow(newLine)
        
        
