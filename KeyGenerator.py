class KeyGenerator():

	def generate_key(self,start_value,max_value,factor):
		key_size = 3
		key = []

		key.append(start_value)

		for i in range(1,key_size):

			key.append(key[i-1]*max_value+factor)

		return key