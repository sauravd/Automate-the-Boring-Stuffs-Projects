# Created by saurav at 21:55 on 2019-07-02

__author__ = "Saurav Dahal"

'''
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to
replace them.
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
The results should be printed to the screen and saved to a new text file.

'''

import os, sys, pyperclip, shelve, re

file_name = input('Enter the name of the template file you wish to use: ')
lib = open('{0}/{1}.txt'.format(os.getcwd(), file_name))
string = lib.read()

#find all madlibbable prompt word
replaced = 0
madlib_regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlib_regex.findall(string)

#For each word, prompt for user replacement then replace it is in the string
for found in matches:
    sub = input('Enter a ' + found + ': ')
    string = string.replace(found,sub, 1)


print(string)