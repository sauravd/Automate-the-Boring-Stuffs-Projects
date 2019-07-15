# Created by saurav at 22:17 on 2019-07-14

__author__ = "Saurav Dahal"

import os, re, shutil

'''
To add a prefix to the start of the filename, such as adding spam_ to
rename eggs.txt to spam_eggs.txt
'''

textFileRegex = re.compile(r"""
    (\w+[.txt]{4})
""", re.VERBOSE)

for file in os.listdir('.'):
    mo=textFileRegex.match(file)

    newFileName = 'spam_'+file

    os.rename(file, newFileName)

    if mo == None:
        continue


    print('Renaming "%s" to "%s"...' %(file, newFileName))
