def quickSort(ls):
	if len(ls) == 1:
		return ls
	pivot = len(ls) - 1
	i = 0
	while i < pivot:
		if ls[i] > ls[pivot]:
			temp = ls[i]
			del ls[i]
			ls.append(temp)
			pivot -= 1
		else:
			i += 1
	if pivot == 0:
		list_new = []
		list_new.append(ls[pivot])
		list_new += quickSort(ls[pivot+1:])
	elif pivot == len(ls) -1:
		list_new = []
		list_new += quickSort(ls[0:pivot])
		list_new.append(ls[pivot])
	else:
		list_new = []
		list_new += quickSort(ls[0:pivot])
		list_new.append(ls[pivot])
		list_new += quickSort(ls[pivot+1:])
	return list_new
	


a=[2,1,3,6,5,7,8]
print quickSort(a)
