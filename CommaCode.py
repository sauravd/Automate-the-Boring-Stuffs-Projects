# Created by saurav at 2019-04-29 in 11:47

__author__ = "Saurav Dahal"

import  ast

def CommaCode(someList):
    newString = ''
    for i in range(len(someList)):
        if i != len(someList)-1:
            newString += someList[i] + ', '
        else:
            newString += 'and ' + someList[i]
    print(newString)






