class heap:
	def __init__(self):
		self.array = []
		self.heap_size = 0
		self.length = 0
	def insert(self,node):
		self.length +=1
		self.heap_size +=1
		self.array = [node]+self.array
		self.max_heapify(0)
	def extract_max(self):
		maxi = self.array[0]
		self.array[0] = self.array[self.length-1]
		self.length -=1
		self.max_heapify(0)
		return maxi
	def increase_key(self,i,keyprime):
		if keyprime < self.array[i].key:
			break
		self.array[i].key = keyprime
		while i >=0 and self.array[i].key > self.array[self.parent(i)].key:
			self.array[i],self.array[self.parent(i)] = self.array[self.parent(i)],self.array[i]
			i = self.parent(i)
	def left(self,i):
		return 2*i+1
	def right(self,i):
		return 2*i+2
	def parent(self,i):
		return int((i-1)/2)
	def build_max_heap(self):
		for i in range(int((self.length-1)/2),-1,-1):
			self.max_heapify(i)
	def max_heapify(self,i):
		l = self.left(i)
		r = self.right(i)
		if l < self.heap_size and self.array[i].key < self.array[l].key:
			largest = l
		else:
			largest = i
		if r < self.heap_size and self.array[largest].key < self.array[r].key:
			largest = r

		if largest != i:
			self.array[i],self.array[largest] = self.array[largest],self.array[i]
			self.max_heapify(largest)
	def heap_sort(self):
		self.build_max_heap()
		for i in range(self.length-1,0,-1):
			self.array[i],self.array[0] = self.array[0],self.array[i]
			self.heap_size -= 1
			self.max_heapify(0)
