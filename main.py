#!/usr/bin/python2
from sys import argv, exit
from Dictionary import Dictionary
import operator

def dictionary_encoding(file_name, dictionary):
    f = open(file_name, 'r')
    nstring = ''
    dicto = dictionary.getdictionary()
    for line in f:
        for word in line.split(" "):
            word = word.rstrip('\n') #.lower()
            if word in dicto:
                nstring = nstring + dicto[word] + ' '
    f.close()
    return nstring


def dictionary_decoding(file_name, dictionary):
    with open(file_name, 'r') as f:
        encoded = f.read()
    normal_dictionary = dictionary.getdictionary()
    print normal_dictionary
    inverted_dictionary = {value: key for key, value in normal_dictionary.iteritems()}
    print inverted_dictionary
    decoded_text = ''
    encoded = encoded.split(' ')[:-1]
    for word in encoded:
        decoded_text = decoded_text + inverted_dictionary[word] + ' '
    return decoded_text

if __name__ == '__main__':
    
    try:
        file_name = argv[1]
    except:
        exit("Couldn't read text file")

    dictionary = Dictionary(file_name)

    #print dictionary.getsortedwords()
    #print dictionary.getdictionary()

    with open('output.txt', 'w') as f:
        f.write(dictionary_encoding(file_name, dictionary))

    print dictionary_decoding('output.txt', dictionary)
