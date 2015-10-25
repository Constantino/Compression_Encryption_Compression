class MultiDictionaryGeneration:
	
	def read_file(self,file_name):
		fileInput = open(file_name, 'r')
		text = fileInput.read()
		print text
