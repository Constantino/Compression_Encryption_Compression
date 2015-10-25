class MultiDictionaryGeneration:
	
	def read_file(self,file_name):
		fileInput = open(file_name, 'r')
		text = fileInput.read()
		print text

	def countWords(text):
		for word in text:
			frequency = frecuencies.get(word, None)
            if frequency == None:
               frequencies[word] = 1
            else:
               frequencies[word] = frequency + 1
        return frequencies