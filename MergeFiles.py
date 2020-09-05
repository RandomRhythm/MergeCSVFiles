import os
import sys
def mergeLogs(strInputFile, strOutputFile):
    global boolHeaderWritten
    f1 = open(strInputFile, 'r', encoding="utf-8") #cp-1252 utf-8
    f2 = open(strOutputFile, 'a+', encoding="utf-8")
    fContents = f1.read()
    f1.close()
    f2.write(fContents)
    f2.close

def mergeLogsLines(strInputFile, strOutputFile):
    global boolHeaderWritten
    f1 = open(strInputFile, 'r', encoding="utf-8") #cp-1252 utf-8
    f2 = open(strOutputFile, 'a+', encoding="utf-8")
    for line in f1:
        if strIncludeOnce in line and boolHeaderWritten == False:
            f2.write(fContents + "\n")
            boolHeaderWritten = True
        elif strIncludeOnce not in line and strExcludeAlways not in line:
            f2.write(fContents + "\n")
    f1.close()
    
    f2.close

strInputPath = "c:\\inputfolderpath\\CSV" #folder path containing CSV files to merge
strOutputPath = "c:\\outputfilepath\\all.csv" #output csv file location
strIncludeOnce = "Name\",\"DisplayName\",\"State\",\"PathName" #include this string once (header row)
boolHeaderWritten = False
strExcludeAlways = "#TYPE Selected.System.Management.ManagementObject" #always exclude from output CSV
for file in os.listdir(strInputPath):
  inputpath = os.path.join(strInputPath, file)
  if os.path.isfile(inputpath):
    if strIncludeOnce == "" and strExcludeAlways == "":
        mergeLogs(inputpath, strOutputPath)
    else:
        mergeLogsLines(inputpath, strOutputPath)
exit()
