# you are given an unsorted array of integers where every integer appears exactly twice
# except for one integer which appears only once. Write an algorithm that finds the integer
# that appears only once

def oddManOut(ls):
	ls1 = []
	for x in range(0, len(ls)):
		ls1.append(0)
	HashMap = {}
	i = 0
	while i < len(ls):
		if ls[i] not in HashMap:
			HashMap[ls[i]] = i
		else:
			ls1[i] += 1
			ls1[HashMap[ls[i]]] += 1
		i += 1
	j = 0
	while j < len(ls1):
		if ls1[j] != 1:
			return ls[j]
		j += 1
	return "invalid array"


def oddManOut_bitwise(ls):
	val = 0
	for x in ls:
		val ^= x
	return val

ls = [1,1,2,2,4,5,6,7,8,9,8,7,6,9,5]
print oddManOut_bitwise(ls)