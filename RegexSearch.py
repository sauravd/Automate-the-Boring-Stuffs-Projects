# Created by saurav at 21:34 on 2019-07-05

__author__ = "Saurav Dahal"

'''
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.
'''

import pprint, re, os

txtFiles = []
for files in os.listdir('.'):
    if files.endswith('.txt'):
        txtFiles.append(files)


UserSuppliedRegex = input("Please provide a regular expression to search:\n")
RegexMatch = re.compile(UserSuppliedRegex, re.I)

fileList = []

for filename in txtFiles:
  open_file = open(filename)
  read_file = open_file.read()
  if RegexMatch.search(read_file):
      fileList.append(filename)



pprint.pprint(fileList)



