#!/usr/bin/python2
from sys import argv, exit
from Dictionary import Dictionary

if __name__ == '__main__':
    
    try:
        file_name = argv[1]
    except:
        exit("Couldn't read text file")

    dictionary = Dictionary(file_name)
    frequencies = dictionary.countWords()
    print frequencies