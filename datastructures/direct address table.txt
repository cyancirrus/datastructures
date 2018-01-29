class pages:
	def __init__(self):
		self.key = 1
		self.data = None
class diction:
	def __init__(self,n):
		self.diction = [None]*n
	def da_search(self,k):
		return self.diction[k]
	def da_delete(self,x):
		self.diction[x] = None
	def da_insert(self,x):
		new_page = pages()
		new_page.data = x
		self.diction[new_page.key] = new_page.data

