def BWT(string):
    
    assert "\0" not in string, "Input string cannot contain null character ('\\0')"
    string += "\0"  # Add end of file marker

    table = [string[n:] + string[:n] for n in xrange(len(string))]
    table = sorted(table)

    return "".join([rotation[-1] for rotation in table])


def invert_BWT(r):

    table = [""] * len(r)  
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  
    s = [row for row in table if row.endswith("\0")][0]  
    return s.rstrip("\0")  

"""
Based on:
https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform
"""