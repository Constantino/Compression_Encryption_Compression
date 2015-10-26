#!/usr/bin/python2
from sys import argv, exit
from Dictionary import Dictionary
import operator

def replaceWords(file_name, dictionary):
    f = open(file_name, 'r')
    nstring = ''
    dicto = dictionary.getdictionary()
    for line in f:
        for word in line.split(" "):
            if word in dicto:
                nstring += dicto[word]
    return nstring

if __name__ == '__main__':
    
    try:
        file_name = argv[1]
    except:
        exit("Couldn't read text file")

    dictionary = Dictionary(file_name)

    #print dictionary.getsortedwords()
    #print dictionary.getdictionary()

    print replaceWords(file_name, dictionary)


