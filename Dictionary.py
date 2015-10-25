class Dictionary:

	def __init__(self, file_name):
		self._filename = file_name

	def read_file(self):
		fileInput = open(self._filename, 'r')
		text = fileInput.read()
		return text

	def countWords(text):
		for word in text:
			frequency = frecuencies.get(word, None)
			if frequency == None:
				frequencies[word] = 1
			else:
				frequencies[word] = frequency + 1
		return frequencies