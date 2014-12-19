#!/usr/bin/env python
import sys
import csv
import webbrowser

#takes the rows of a .csv file and only outputs
# the first X rows. good for shortening a .csv
# for testing. make sure to use a redirect
# into a new file: python getXlines.py 10 > new.csv

lines = int(sys.argv[2])
x = 0
with open(sys.argv[1]) as inFile:
    for row in csv.reader(inFile):
        outString = str(row)
        outString = outString.replace("[", "")
        outString = outString.replace("]", "")
        outString = outString.replace("'", "")
        outString = outString.replace(" ", "")
        print outString
        x += 1
        if x >= lines:
            break
