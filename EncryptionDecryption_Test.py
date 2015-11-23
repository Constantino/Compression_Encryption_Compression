from KeyGenerator import KeyGenerator
from ReducedArrayEncryption import ReducedArrayEncryption 
from ReducedArrayDecryption import ReducedArrayDecryption

start_value = 3
max_value = 10 
factor = 4

k = KeyGenerator()
key = k.generate_key(start_value,max_value,factor)
print "key: ",key

string = "mytextisjusttext"
print "string: ",string

a = ReducedArrayEncryption(string,key)
text_encrypted = a.encrypt()
print "text_encrypted",text_encrypted

new_text = a.get_text_encrypted(text_encrypted[1])

b = ReducedArrayDecryption(new_text,key,text_encrypted[0]) 

print "original text: ", b.decrypt()

