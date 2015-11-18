import heapq
from collections import Counter

class Node():

	def __init__(self, name, frequency):
		self._name = name
		self._frequency = frequency
		self._left = None
		self._right = None

	def setChildren(self, left_node, right_node):
		self._left = left_node
		self._right = right_node

	def getChildren(self):
		return self._left, self._right

	def __cmp__(self, frequency):
		return cmp(self._frequency, frequency)

	def __repr__(self):
		return "Key: %s Value: %s" % (self._name, self._frequency)

class HuffmanCode:
    def __init__(self, string):
        self._codes={}
        self._string = string

    def create_tree(self):
    	nodes = [Node(e, f) for e, f in Counter(self._string).items()]
    	heapq.heapify(nodes)
    	while len(nodes)>1:
    		left_node = heapq.heappop(nodes)
    		right_node = heapq.heappop(nodes)
    		new_node = Node(left_node._name+right_node._name, left_node._frequency+right_node._frequency)		
    		new_node.setChildren(left_node, right_node)
    		#print new_node
    		heapq.heappush(nodes, new_node)
    	return nodes[0]

    def get_codes(self, node, code):
        if node is not None:
            if node._left is None and node._right is None:
                self._codes[node._name] = code
            self.get_codes(node._left, code + '0')
            self.get_codes(node._right, code + '1')

    def huffman_code(self):
        root = self.create_tree()
        self.get_codes(root, '')
        return self._codes

def encode(string):
    huffman_code = HuffmanCode(string)
    codes = huffman_code.huffman_code()
    encoded = ""
    for e in string:
        encoded += codes[e]
    new_binary = [encoded[i:i+8] for i in xrange(0, len(encoded), 8)]
    new_string = [chr(int(binary, 2)) for binary in new_binary]
    new_string = "".join(new_string)
    return new_string
        
def decode(encoded):
    return encoded