#---------------------------------
#Given an array of integers, find two numbers such that they add up to a specific target number.
#---------------------------------

def twoSum(ls,target):
	if len(ls) < 2:
		return "list should be at least two values"
	result = []
	i = 0 
	differenceMap = {}
	while i < len(ls):
		if ls[i] not in differenceMap:
			differenceMap[target - ls[i]] = i
		else:
			result.append(differenceMap[ls[i]]+1)
			result.append(i + 1)
			break
		i += 1
	print differenceMap
	if len(result) != 2:
		return "Do not exist"
	else:
		return result

ls = [2,7,11,15]
target = 17

print twoSum(ls,target)

