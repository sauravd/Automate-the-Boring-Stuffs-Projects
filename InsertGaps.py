# Created by saurav at 13:30 on 2019-07-19

__author__ = "Saurav Dahal"

"""
Write a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps
into numbered files so that a new file can be added.
"""

import os, shutil, re


folder = input("Please enter absolute path to a folder to fill in the gaps:\n ")
newFileName = input("Please enter the new file name in format 'spam00x.txt':\n ")
#prefix = input("Enter a prefix of file type:\n")
#extension = input("Enter a extension of file type:\n")
fileprefix = re.compile(r'''
    (\w*)
    ([00]{2})
    (\d*)
    ([.txt]{4})
''', re.VERBOSE)

match2 = fileprefix.match(newFileName)
firstPart2 = match2.group(1)
zeroPart2 = match2.group(2)
numberPart2 = match2.group(3)
extensionPart2 = match2.group(4)

for files in os.listdir(folder):
    match = fileprefix.search(files)

    if match == None:
        continue

    firstPart = match.group(1)
    zeroPart = match.group(2)
    numberPart = match.group(3)
    extensionPart = match.group(4)

    numberList = []
    numberList.append(numberPart)

    if numberPart2 in numberList:
        print("Given file number already exists!, give a new file number.")
        exit(1)
    else:
        open(newFileName, 'w')







