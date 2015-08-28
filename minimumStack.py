#-----------------------------
#Design a stack that supports push, pop, and retrieving the minimum element in constant time. Can you do this?
#-----------------------------

class MiniStack:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
		self.curMin = float("inf")

	def push(self, item):
		if item < self.curMin:
			self.curMin = item
			self.stack1.append(item)
			self.stack2.append(item)
		else:
			self.stack1.append(item)

	def pop(self):
		if self.curMin == self.stack1[len(self.stack1)-1]:
			self.stack1.pop()
			self.stack2.pop()
			self.curMin = self.stack2[len(self.stack2)-1]
		else:
			self.stack1.pop()

	def findMin(self):
		return self.curMin

	def printStack1(self):
		for i in self.stack1:
			print i

	def printStack2(self):
		for i in self.stack2:
			print i

s1 = MiniStack()
s1.push(2)
s1.push(5)
s1.push(1)
s1.printStack1()
s1.printStack2()

s1.printStack1()
print s1.findMin()

