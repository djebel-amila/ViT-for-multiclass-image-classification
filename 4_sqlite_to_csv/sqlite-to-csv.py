# This Python script will convert a specified sqlite.db database file to csv and keep only the relevant data for our training dataset, i.e. the images names and their label as manually assigned in tkteach. 
# It will write a new .csv file named after the original .db file. 
# It will place the duplicated and resized image files in a new directory named after the original directory + "-resized" + the specified dimensions. 
# use: In terminal, run program followed by the path to the sqlite database, i.e.: 
# $python sqlite-to-csv.py storage.db
# will create a new file named "storage.csv" containing the images names on the first column and the category on the secnod.

import csv
import sqlite3
import numpy

import sys
db = sys.argv[1]

# open connection to sqlite database
#sqliteConnection = sqlite3.connect('storage.db')
sqliteConnection = sqlite3.connect(db)
# query to get and join the column "ImageName" from the "images" table and the "category_id" from the "labels" table and use "id" and "image_id" as joining key (to match the objects)
#the following query gets the labels as int (0,1,2…)
#sql_query = """select labels.category_id, images.ImageName from labels INNER JOIN images on labels.image_id = images.id;"""
#the following query gets the labels as nicenames
sql_query = """select images.ImageName, categories.categoryName FROM images INNER JOIN labels ON images.id = labels.image_id INNER JOIN categories ON categories.id = labels.category_id;"""
# create a cursor to access the tables’ contents
cursor = sqliteConnection.cursor()
# store in a sqlite3.cursor object
rows = cursor.execute(sql_query)


# create a new csv file
with open(str(db.split(".")[0]) + ".csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    for row in rows:
        # split category_id/labels so that only the last item in the list (the label without its keyboard shortcut) is written
        #a = str(row[1]) <— replace by this to write full labels.category_id
        a = row[1].split(" ")
        # split imageName/imagePath so that only the actual filename is written into the csv file
        #b = str(row[0]) <— replace by this to write full imagePath
        b = row[0].split("/")
        newRow = b[len(b)-1], a[len(a)-1]
        csv_writer.writerow(newRow)

# close connection to sqlite database
sqliteConnection.close()


