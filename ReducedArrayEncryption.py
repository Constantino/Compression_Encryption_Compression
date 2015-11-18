class ReducedArrayEncryption:

	def __init__(self,rle_output, primary_key):

		self._ta_key = []
		self._rle_output = rle_output
		self._primary_key = primary_key

	def encrypt(self):

		self.fill_ta_key(self._rle_output)

		data_encrypted = []
		i = 1
		l = 1
		len_rle_output = len(self._rle_output)

		while i <= len_rle_output:
			s = 0
			for j in range(3):
				s += ord(self._rle_output[i])*self._primary_key[j]
			data_encrypted.append(s)
			i+=3

		return self._ta_key, data_encrypted
	
	def fill_ta_key(self,rle_output):
		for e in self._rle_output:
			if e not in self._ta_key:
				self._ta_key.append(e)


