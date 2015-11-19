#!/usr/bin/python2
#@author: adominguez
#@date: 20151025 17:10:42
class Compression: 
    from itertools import groupby
    import itertools

    def __init__(self, encode, decode):
        self.word=encode
        self.lst=decode


    #Compresion BWT
    def bwt(self):
    	assert "\0" not in word, "Input string cannot contain null character ('\\0')"
    	word += "\0"  
    	table = sorted(word[i:] + word[:i] for i in range(len(word)))    
    	last_column = [row[-1:] for row in table] 
    	return "".join(last_column) 

    # #Compresion Reversa BWT
    def inverseBWT(r):
        table = [""] * len(r)
        for i in range(len(r)):
            table = sorted(r[i] + table[i] for i in range(len(r)))  
        s = [row for row in table if row.endswith("\0")][0]
        return s.rstrip("\0") 


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

    #Compression reversa RLE
    #recibe una lista tipo [('A',15)('B',2)...('s',n)]
    def reverseRLE(self):
        q = ""
        for character, count in lst:
            q += character * count
        return q



