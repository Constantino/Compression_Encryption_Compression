#!/usr/bin/python2
from sys import argv, exit
from Person import Person
import timeit

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

    
    ###############################################################################################
    ####  Compression-Encryption-Compression

    alice = Person('Alice')
    bob = Person('Bob')
    encoded = alice.send(original_text)

    ###############################################################################################
    ####  Decompression-Decryption-Decompression

    recovered_text = bob.receive(encoded)
    print "Recovered text"
    print recovered_text

    ###############################################################################################

    toc=timeit.default_timer()

    original_text_size, compressed_text_size, compression_ratio = compression_ratio(original_text, encoded[0])

    print "Original text size:", original_text_size, "bytes"
    print "Compressed text size:", compressed_text_size, "bytes"
    print "Compression ratio:", compression_ratio 
    print "Time elapsed:", toc-tic, "seconds"