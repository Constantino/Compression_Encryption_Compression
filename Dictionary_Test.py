from Dictionary import *
from sys import argv

try:
    file_name = argv[1]
except:
    exit("Couldn't read text file")

# Original text
with open(file_name, 'r') as f:
    original_text = f.read()

print "Original"
print original_text

# Create dictionary
dictionary = Dictionary(original_text)

# Dictionary encoding
encoded_text = dictionary_encoding(original_text, dictionary)
print "Dictionary encoded"
print encoded_text
with open('dictionary_encoding_output.txt', 'w') as f:
    f.write(encoded_text)

# Dictionary decoding
decoded_text = dictionary_decoding(encoded_text, dictionary)
print "Dictionary decoded"
print decoded_text
with open('dictionary_decoding_output.txt', 'w') as f:
    f.write(decoded_text)