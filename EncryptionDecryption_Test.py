from KeyGenerator import KeyGenerator
from ReducedArrayEncryption import ReducedArrayEncryption 
from ReducedArrayDecryption import ReducedArrayDecryption

start_value = 3
max_value = 10 
factor = 4

k = KeyGenerator()
key = k.generate_key(start_value,max_value,factor)
print key

string = "sdfsdf"
a = ReducedArrayEncryption(string,key)
text_encrypted = a.encrypt()
print text_encrypted


b = ReducedArrayDecryption(text_encrypted[1],key,text_encrypted[0])
print b.decrypt()
