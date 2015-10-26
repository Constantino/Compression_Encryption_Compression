#!/usr/bin/python2
#@author: adominguez
#@date: 20151025 17:10:42
from itertools import groupby
import itertools

#Compresion BWT
def bwt(word):
	assert "\0" not in word, "Input string cannot contain null character ('\\0')"
	word += "\0"  
	table = sorted(word[i:] + word[:i] for i in range(len(word)))    
	last_column = [row[-1:] for row in table] 
	return "".join(last_column) 


#Compresion RLE
def rle(s):
    count = 1
    prev = ''
    lst = []
    strCount = ''
    for character in s:
        if character != prev:
            if prev:
                entry = (count,prev)
                lst.append(entry)
                #print lst

            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (count,character)
        lst.append(entry)
        #Se elimina ultimo elemento del array (espacio)
        lst.pop()
        word = ''.join(itertools.imap(str, itertools.chain(*lst)))
    return word


if __name__ == '__main__':
	
	s = "^BANANA"
	print bwt(s)
	print rle(bwt(s))
