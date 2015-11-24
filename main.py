#!/usr/bin/python2
from sys import argv, exit
import timeit
from Dictionary import Dictionary
from HuffmanCoding import encode as huffman_encode
from HuffmanCoding import decode as huffman_decode
from BWT import BWT, invert_BWT
from RLE import rle, invert_rle
from KeyGenerator import KeyGenerator
from ReducedArrayEncryption import ReducedArrayEncryption 
from ReducedArrayDecryption import ReducedArrayDecryption

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


def dictionary_decoding(encoded, dictionary):
#    with open(file_name, 'r') as f:
#        encoded = f.read()
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

    ###############################################################################################
    ####  Compression-Encryption-Compression

    # Dictionary encoding
    encoded_text = dictionary_encoding(file_name, dictionary)
    print "Dictionary encoded", encoded_text
    with open('dictionary_encoding_output.txt', 'w') as f:
        f.write(encoded_text)

    # Burrows-Wheeler Transform
    bwt_encoded_text = BWT(encoded_text)
    print "BWT", bwt_encoded_text

    # Run-length encoding
    rle_encoded_text = rle(bwt_encoded_text)
    print "RLE", rle_encoded_text

    ###### Encryption ######
    start_value = 9
    max_value = 83
    factor = 4

    k = KeyGenerator()
    key = k.generate_key(start_value,max_value,factor)
    print key

    a = ReducedArrayEncryption(rle_encoded_text,key)
    encrypted = a.encrypt()
    encrypted_text = a.get_text_encrypted(encrypted[1])
    print "Encrypted", encrypted_text

    ########################

    # Huffman coding
    huffman_encoded_text, huffman_root = huffman_encode(encrypted_text) # The root will be necessary to decode
    print "Huffman", huffman_encoded_text
    with open('huffman_encoded_text', 'wb') as f:
        f.write(huffman_encoded_text)


    ###############################################################################################
    ####  Decompression-Decryption-Decompression

    # Huffman decoding
    huffman_decoded_text = huffman_decode(huffman_encoded_text, huffman_root)
    print "Huffman decoded"
    print huffman_decoded_text

    ###### Decryption ######
    b = ReducedArrayDecryption(encrypted_text,key,encrypted[0]) 
    decrypted_text = b.decrypt()
    print "Decrypted text", decrypted_text
    ########################

    # Run-length decoding
    rle_decoded_text = invert_rle(decrypted_text)
    print "RLE inverse", rle_decoded_text    

    # Burrows-Wheeler Transform
    bwt_decoded_text = invert_BWT(rle_decoded_text)
    print "BWT inverse", bwt_decoded_text

    # Dictionary decoding
    #decoded_text = dictionary_decoding('dictionary_encoding_output.txt', dictionary)
    decoded_text = dictionary_decoding(bwt_decoded_text, dictionary)
    print "Dictionary decoded", decoded_text
    with open('dictionary_decoding_output.txt', 'w') as f:
        f.write(decoded_text)

    ###############################################################################################

    toc=timeit.default_timer()

    original_text_size, compressed_text_size, compression_ratio = compression_ratio(original_text, rle_encoded_text)

    print "Original text size:", original_text_size, "bytes"
    print "Compressed text size:", compressed_text_size, "bytes"
    print "Compression ratio:", compression_ratio 
    print "Time elapsed:", toc-tic, "seconds"