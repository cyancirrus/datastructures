class heap:
	def __init__(self,array:list):
		self.array = array
		self.heap_size = len(self.array)
		self.length = len(self.array)
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
		if l < self.heap_size and self.array[i] < self.array[l]:
			largest = l
		else:
			largest = i
		if r < self.heap_size and self.array[largest] < self.array[r]:
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

