# Created by saurav at 11:32 on 2019-07-15

__author__ = "Saurav Dahal"

import os, re

"""
To remove the zeros from files such as spam0042.txt
"""

zeroCaptureRegex = re.compile(r"""
                   (\w+)
                   ([0]{2})
                   (\d{2})
                   ([.txt]{4})     
""", re.VERBOSE)

for file in os.listdir('.'):
    mo = zeroCaptureRegex.search(file)

    if mo == None:
        continue

    firstPart = mo.group(1)
    zeroPart = mo.group(2)
    numberPart = mo.group(3)
    extensionPart = mo.group(4)

    newFileName = firstPart + numberPart + extensionPart

    os.rename(file, newFileName)

    print('Renaming "%s" to "%s"...' %(file, newFileName))
