import heapq
from collections import Counter

class Node():

	def __init__(self, item, weight):
		self._item = item
		self._frequency = frequency

	def children(self, left_node, right_node):
		self._left = left_node
		self._right = right_node

	def __cmp__(self, frequency):
		return cmp(self._frequency, frequency)

	def __repr__(self):
		return "%s - %s \t %s - %s" % (self._item, self._frequency, self._left, self._right)

def create_tree(string):
	return string