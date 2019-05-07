# Created by saurav at 2019-05-06 in 14:26

__author__ = "Saurav Dahal"


# takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


def printTable(someList):
    colWidths = [0] * len(someList)
    for i in range(len(someList)):
        for j in range(len(someList[i])):
            if len(someList[i][j]) > colWidths[i]:
                colWidths[i] = len(someList[i][j])

    for i in range(len(someList[0])):
        for j in range(len(someList)):
            print(someList[j][i].rjust(colWidths[j]), end=' ')
        print()

printTable(tableData)


