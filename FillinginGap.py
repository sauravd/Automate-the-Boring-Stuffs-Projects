# Created by saurav at 14:31 on 2019-07-18

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
#prefix = input("Enter a prefix of file type:\n")
#extension = input("Enter a extension of file type:\n")
fileprefix = re.compile(r'''
    (\w*)
    ([00]{2})
    (\d*)
    ([.txt]{4})
''', re.VERBOSE)

number = 1

for files in os.listdir(folder):
    match = fileprefix.search(files)

    if match == None:
        print("No pattern matched !!")
        continue

    firstPart = match.group(1)
    zeroPart = match.group(2)
    numberPart = match.group(3)
    extensionPart = match.group(4)

    numberList = []
    numberList.append(numberPart)


    newFileName = (firstPart + zeroPart + "%d" %number + extensionPart)
    number += 1

    oldFiles = os.path.join(folder, files)
    newFile = os.path.join(folder, newFileName)


    print('Renaming %s to %s...' %(oldFiles, newFileName))








