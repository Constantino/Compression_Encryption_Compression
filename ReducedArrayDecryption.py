class ReducedArrayDecryption:

	def __init__(self, data, primary_key, ta_key):
		self._data = data
		self._primary_key = primary_key
		self._ta_key = ta_key

	def decrypt(self):

		len_data = len(self._data)

		original_data = []

		len_ta_key = len(self._ta_key)

		#for i in range(len_data):
		flag = 1
		EST = 0
		
		s1,s2,s3 = 0,0,0
		print self._ta_key
		while flag:
			
			t = [0,0,0]
			t[0] = self._ta_key[s1]
			t[1] = self._ta_key[s2]
			t[2] = self._ta_key[s3]
			EST = 0
			for k in range(3):
				EST += ord(t[k]) * self._primary_key[k]
			print "--- comb: ", t[0]," ", t[1]," ", t[2]
			print "*** est: ",EST," - ",self._data[0]
			if EST == self._data[0]:
				print "equal, data found"
				flag = 0
			else:
				s1 += 1
				if s1 >= len_ta_key:
					s2 += 1
					s1 = 0	
				if s2 >= len_ta_key:
					s3 += 1
					#s1 = 0
					s2 = 0
				if s3 >= len_ta_key:
					#s1 = 1
					#s2 = 1
					s3 = 0

		return original_data