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

def create_tree(string):
	nodes = [Node(e, f) for e, f in Counter(string).items()]
	heapq.heapify(nodes)
	while len(nodes)>1:
		left_node = heapq.heappop(nodes)
		right_node = heapq.heappop(nodes)
		new_node = Node(left_node._name+right_node._name, left_node._frequency+right_node._frequency)		
		new_node.setChildren(left_node, right_node)
		#print new_node
		heapq.heappush(nodes, new_node)
	return nodes[0]

# Dictionary with Huffman codes
leafs = {}

def get_codes(node, code):
    if node is not None:
        if node._left is None and node._right is None:
            leafs[node._name] = code
        get_codes(node._left, code + '0')
        get_codes(node._right, code + '1')

def huffman_code(string):
    root = create_tree(string)
    get_codes(root, '')
    return leafs