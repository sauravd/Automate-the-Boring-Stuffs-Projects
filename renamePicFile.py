# Created by saurav at 13:33 on 2019-07-13

__author__ = "Saurav Dahal"




'''
This program renames a given picture(.jpeg) file into desired name. 
The picture has been imported from a mobile phone and has a random name, 
which will be renamed by this program.
'''

import os, re, shutil

filePattern = re.compile(r"""^([DikshyaDep2019]{14})_
                        (\d)
                        (.*)   
""", re.VERBOSE)

getDirectory = input('Please input the desired directory to rename file: \n')
dirFullPath = os.path.join('/', 'Users', 'saurav', getDirectory)
print(dirFullPath)

i = 1

#Search for the file type in the given directory
for picFile in os.listdir(dirFullPath):
    mo = filePattern.search(picFile)

    if mo == None:
        print("No pattern matched !!")
        continue

    #Rename file name to desired option

    newFileName = 'DikshyaDep2019_%d.jpg' %i
    i += 1


    picFile = os.path.join(dirFullPath, picFile)
    newFileName = os.path.join(dirFullPath, newFileName)

    os.rename(picFile, newFileName)

    #Renaming the files,
    print('Renaming "%s" to "%s"...' %(picFile, newFileName))
