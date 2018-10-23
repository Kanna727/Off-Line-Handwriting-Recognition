#!/usr/bin/python3
from PreprocessingCodes.showpoints import showpoints
from PreprocessingCodes.interpolation import interpolation
from FeatureExtractionCodes.features import features
import csv
import os

filename = input('Enter the filepath:')

d = showpoints('Original Plot', filename)
d = interpolation(d)
final_features = features(d)
target = int(input("Enter stroke label(For only training):"))
final_features.insert(0, target)
print(final_features)
print(len(final_features))
#'/home/karthik/Documents/vscode/minorproject/On-Line-Handwriting-Recognition/Samples/1.txt'


title_row = ['Label']
for i in range(360):
    title_row.append(i + 1)
filename = os.path.expanduser("~//Desktop//training_dataset.csv")
# print(filename)
if os.path.exists(filename):
    # print('exists')
    append_write = 'a' # append if already exists...
else:
    # print('not exist')
    append_write = 'w+' # make a new file if not

myFile = open(filename, append_write, newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(final_features)
myFile.close()
# d = smoothing(d, 4, filename)
