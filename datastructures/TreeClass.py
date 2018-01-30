class node:
	def __init__(self):
		self.right = None
		self.left = None
		self.parent = None
		self.data = None

class tree():
	def __init__(self):
		self.cur_node = None
		self.root = None
	def set_root(self,data):
		new_node = node()
		new_node.data  = data
		self.cur_node = new_node
		self.root = new_node
	def add_left_b(self,data):
		new_node = node()
		new_node.data = data
		self.cur_node.left = new_node
		new_node.parent = self.cur_node
	def add_right_b(self,data):
		new_node = node()
		new_node.data = data
		self.cur_node.right = new_node
		new_node.parent = self.cur_node
	def move_branch_right(self):
		self.cur_node = self.cur_node.right
	def move_branch_left(self):
		self.cur_node = self.cur_node.left
	def move_up(self):
		self.cur_node = self.cur_node.parent
	def move_root(self):
		self.cur_node = self.root
	def iterative_tree_search(self,k):
		while x and k != x.key:
			if k> x.key:
				x = x.left
			else:
				x = x.right
		return x
	def tree_search(self,k):
		if not(self) or self.key == k:
			return  self
		if k < self.key:
			return tree_search(self.left,k)
		else:
			return tree_search(self.right,k)
			


	def in_order_tree_walk(x):
		if x:
			in_order_tree_walk(x.left())
			pint x.key
			in_order_tree_walk(x.right())

