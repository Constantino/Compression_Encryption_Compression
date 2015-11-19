class ReducedArrayEncryption:

	def __init__(self,rle_output, primary_key):

		self._ta_key = []
		self._rle_output = rle_output
		self._primary_key = primary_key
		self._len_rle_output = len(rle_output)

	def encrypt(self):

		self.fill_ta_key(self._rle_output)
		self.pre_process_rle()

		data_encrypted = []
		i = 0
		
		while i < self._len_rle_output:
			s = 0
			for j in range(3):
				s += ord(self._rle_output[i+j])*self._primary_key[j]
			data_encrypted.append(s)
			i+=3

		return self._ta_key, data_encrypted
	
	def pre_process_rle(self):
		f = self._len_rle_output - self._len_rle_output%3 + 3
		self._rle_output = self._rle_output.ljust(f,'0')

	def fill_ta_key(self,rle_output):
		for e in self._rle_output:
			if e not in self._ta_key:
				self._ta_key.append(e)


