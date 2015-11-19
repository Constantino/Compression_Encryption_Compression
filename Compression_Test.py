from Compression import Compression 

x = Compression("BANANA", [('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])

print x.bwt()
print x.rle(bwt())
print x.reverseRLE()
print x.reverseBWT(reverseRLE())