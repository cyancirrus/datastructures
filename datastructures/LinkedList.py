class node:
	def __init__(self):
		self.data = None
		self.next = None
		self.previous = None

class linked_list:
	def __init__(self):
		self.cur_node = None
	def head(self):
		self.head = None
	def last(self):
		self.last = None
	def add_node(self,data):
		new_node = node()
		new_node.data = data
		new_node.next = self.head
		if (self.cur_node):
			new_node.previous = self.last
			self.last.next = new_node
			self.head.previous = new_node
		elif not(self.cur_node):
			self.head = new_node
			self.cur_node = new_node
		self.last = new_node
	def next_node(self):
		self.cur_node = self.cur_node.next
	def prev_node(self):
		self.cur_node = self.cur_node.previous
	def list_search(self,k):
		x=self.head
		while x and x.data != k:
			x = x.next
		return x

