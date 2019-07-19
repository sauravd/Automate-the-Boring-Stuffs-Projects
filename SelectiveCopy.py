# Created by saurav at 13:25 on 2019-07-18

__author__ = "Saurav Dahal"

"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.
"""

import os, shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)

    destination = input("Enter destination folder's absolute filepath: ")

    for folders, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.txt'):
                shutil.copy(os.path.join(folder, filename), destination)





selectiveCopy('/Users/saurav/PycharmProjects/pythonplayground')