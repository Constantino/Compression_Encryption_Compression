import heapq
from collections import Counter, OrderedDict

class Node():

	def __init__(self, item, frequency):
		self._item = item
		self._frequency = frequency

	def children(self, left_node, right_node):
		self._left = left_node
		self._right = right_node

	def __cmp__(self, frequency):
		return cmp(self._frequency, frequency)

	def __repr__(self):
		return "%s-%s" % (self._item, self._frequency)

def create_tree(string):
	nodes = [Node(e, f) for e, f in Counter(string).items()]
	return nodes