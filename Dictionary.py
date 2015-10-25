class Dictionary:

    def __init__(self, file_name):
        self._filename = file_name

    def countWords(self):
        f = open(self._filename, 'r')
        frequencies = dict()
        for line in f:
            for word in line.split():
                frequency = frequencies.get(word, None)
                if frequency == None:
                    frequencies[word] = 1
                else:
                    frequencies[word] = frequency + 1
        
        return frequencies
