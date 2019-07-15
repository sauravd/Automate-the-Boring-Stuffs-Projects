# Created by saurav at 10:57 on 2019-07-15

__author__ = "Saurav Dahal"

import os, re, shutil

spamHeaderRegex = re.compile(r"""^
    (_)
    (\w*)
    ([.py]{3})
""", re.VERBOSE)

for file in os.listdir('.'):
    mo = spamHeaderRegex.search(file)

    if mo == None:
        continue

    beforePart = mo.group(1)
    afterPart = mo.group(2)
    extensionPart = mo.group(3)

    newFileName = afterPart + extensionPart


    os.rename(file, newFileName)

    print('Renaming "%s" to "%s"...' %(file, newFileName))