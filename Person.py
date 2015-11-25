from Dictionary import *
from HuffmanCoding import encode as huffman_encode
from HuffmanCoding import decode as huffman_decode
from BWT import BWT, invert_BWT
from RLE import rle, invert_rle
from KeyGenerator import KeyGenerator
from ReducedArrayEncryption import ReducedArrayEncryption 
from ReducedArrayDecryption import ReducedArrayDecryption

class Person():
    def __init__(self, name):
        self._name = name

    def send(self, original_text):
        print "original text"
        print original_text

        # Create dictionary
        dictionary = Dictionary(original_text)

        # Dictionary encoding
        encoded_text = dictionary_encoding(original_text, dictionary)
        print "Dictionary encoded"
        print encoded_text
        with open('Results/dictionary_encoding_output.txt', 'w') as f:
            f.write("Encoded text: \n")
            f.write(encoded_text)
        with open('dictionary_encoding_output.txt', 'w') as f:
            f.write(encoded_text)

        # Burrows-Wheeler Transform
        bwt_encoded_text = BWT(encoded_text)
        print "BWT"
        print bwt_encoded_text

        # Run-length encoding
        rle_encoded_text = rle(bwt_encoded_text)
        print "RLE"
        print rle_encoded_text

        ###### Encryption ######
        start_value = 9
        max_value = 83
        factor = 4

        k = KeyGenerator()
        key = k.generate_key(start_value,max_value,factor)
        #print key

        a = ReducedArrayEncryption(rle_encoded_text,key)
        encrypted = a.encrypt()
        encrypted_text = a.get_text_encrypted(encrypted[1])
        print "Encrypted"
        print encrypted_text

        ########################

        # Huffman coding
        huffman_encoded_text, huffman_root = huffman_encode(encrypted_text) # The root will be necessary to decode
        print "Huffman"
        print huffman_encoded_text
        with open('huffman_encoded_text', 'wb') as f:
            f.write(huffman_encoded_text)

        return [huffman_encoded_text, huffman_root, key, encrypted, dictionary]


    def receive(self, encoded):

        huffman_encoded_text, huffman_root, key, encrypted, dictionary = encoded

        # Huffman decoding
        huffman_decoded_text = huffman_decode(huffman_encoded_text, huffman_root)
        print "Huffman decoded"
        print huffman_decoded_text

        ###### Decryption ######
        b = ReducedArrayDecryption(huffman_decoded_text,key,encrypted[0]) 
        decrypted_text = b.decrypt()
        print "Decrypted text"
        print decrypted_text
        ########################

        # Run-length decoding
        rle_decoded_text = invert_rle(decrypted_text)
        print "RLE inverse"
        print rle_decoded_text    

        # Burrows-Wheeler Transform
        bwt_decoded_text = invert_BWT(rle_decoded_text)
        print "BWT inverse"
        print bwt_decoded_text

        # Dictionary decoding
        decoded_text = dictionary_decoding(bwt_decoded_text, dictionary)
        #print "Dictionary decoded"
        #print decoded_text
        with open('dictionary_decoding_output.txt', 'w') as f:
            f.write(decoded_text)

        return decoded_text
