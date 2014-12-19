#!/usr/bin/env python
import sys
import csv
import webbrowser

strBuffer = []
levelBuffer = ""
outString = ""
numFrTerms = 0
numSpTerms = 0
numJuTerms = 0
numSrTerms = 0
sameLevelTerm = False

anchorKey = ""
currentKey = ""

#F1, F2, So1, So2, J1, etc.
#major/notstudent/graduated
#print "Fr1,Fr2,So1,So2,Ju1,Ju2,Se1,Se2"
with open(sys.argv[1]) as inFile:
    for row in csv.reader(inFile):
        currentKey = row[0]
        #test case for first iteration included
        if anchorKey is "":
            anchorKey = row[0]
            strBuffer.append(row)
        else:
            if currentKey is anchorKey:
                strBuffer.append(row)
            else:
                tempFrTerms = 0
                tempSpTerms = 0
                tempJuTerms = 0
                tempSrTerms = 0
                #do many things
                #go through the buffer and how many times student
                # was in each level
                for rowBuffer in strBuffer:
                    #count # of terms student was in each level
                    tempLevel = rowBuffer[3]
                    if tempLevel is "Senior":
                        tempSrTerms += 1
                    elif tempLevel is "Junior":
                        tempJuTerms += 1
                    elif tempLevel is "Sophomore":
                        tempSpTerms += 1
                    elif tempLevel is "Freshman":
                        tempFrTerms += 1
                if tempSrTerms > numSrTerms:
                    numSrTerms = tempSrTerms
                if tempJuTerms > numJuTerms:
                    numJuTerms = tempJuTerms
                if tempSpTerms > numSpTerms:
                    numSpTerms = tempSPTerms
                if tempFrTerms > numFrTerms:
                    numFrTerms = tempFrTerms
                #update anchor
                anchorKey = currentKey
    #add all to string
    for x in range(0, numFrTerms):
        outString += "Fr"+str(x+1)
    for x in range(0, numSpTerms):
        outString += "Sp"+str(x+1)
    for x in range(0, numJuTerms):
        outString += "Ju"+str(x+1)
    for x in range(0, numSrTerms):
        outString += "Sr"+str(x+1)
    print outString
    outString = ""
            
    
#something to notify us the program is finished.
#webbrowser.open("https://www.youtube.com/watch?v=pmGCDVKQgyk")
