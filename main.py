#!/usr/bin/python2
from sys import argv, exit

if __name__ == 'main':
    
    try:
        file_name = argv[1]
    except:
        exit("Couldn't read text file")

    dictionary = Dictionary(file_name)