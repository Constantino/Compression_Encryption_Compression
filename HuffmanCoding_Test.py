from HuffmanCoding import encode as huffman_encode
from HuffmanCoding import decode as huffman_decode


text = "l"

# Huffman coding
huffman_encoded_text, huffman_root = huffman_encode(text) # The root will be necessary to decode
print "Huffman", huffman_encoded_text

# Huffman decoding
huffman_decoded_text = huffman_decode(huffman_encoded_text, huffman_root)
print "Huffman decoded", huffman_decoded_text



