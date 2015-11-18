from KeyGenerator import KeyGenerator
from sys import argv

start_value = int(argv[1])
max_value = int(argv[2])
factor = int(argv[3])

k = KeyGenerator()

print k.generate_key(start_value,max_value,factor)