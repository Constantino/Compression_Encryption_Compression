#!/usr/bin/python2
from sys import argv, exit
import timeit
from Dictionary import Dictionary
from Compression import bwt, rle
from HuffmanCoding import *

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
    inverted_dictionary = {value: key for key, value in normal_dictionary.iteritems()}
    decoded_text = ''
    encoded = encoded.split(' ')[:-1]
    for word in encoded:
        decoded_text = decoded_text + inverted_dictionary[word] + ' '
    return decoded_text


def compression_ratio(original_text, compressed_text):
    # Original text's size
    original_text_size = original_text.__sizeof__() - 37
    # Compressed text size
    compressed_text_size = compressed_text.__sizeof__() - 37
    # Compression ratio
    compression_ratio = float(original_text_size) / float(compressed_text_size)
    return original_text_size, compressed_text_size, compression_ratio


if __name__ == '__main__':
    
    try:
        file_name = argv[1]
    except:
        exit("Couldn't read text file")

    # Original text
    with open(file_name, 'r') as f:
        original_text = f.read()

    tic=timeit.default_timer()

    # Create dictionary
    dictionary = Dictionary(original_text)

    # Dictionary encoding
    encoded_text = dictionary_encoding(file_name, dictionary)
    #print encoded_text
    with open('dictionary_encoding_output.txt', 'w') as f:
        f.write(encoded_text)

    # Burrows-Wheeler Transform
    bwt_encoded_text = bwt(encoded_text)
    #print bwt_encoded_text

    # Run-length encoding
    rle_encoded_text = rle(bwt_encoded_text)
    #print rle_encoded_text

    # Huffman coding
    huffman_code = create_tree(rle_encoded_text)

    # Dictionary decoding
    decoded_text = dictionary_decoding('dictionary_encoding_output.txt', dictionary)
    #print decoded_text
    with open('dictionary_decoding_output.txt', 'w') as f:
        f.write(decoded_text)

    toc=timeit.default_timer()

    original_text_size, compressed_text_size, compression_ratio = compression_ratio(original_text, rle_encoded_text)

    print "Original text size:", original_text_size, "bytes"
    print "Compressed text size:", compressed_text_size, "bytes"
    print "Compression ratio:", compression_ratio 
    print "Time elapsed:", toc-tic, "seconds"