import random

def medianOfArray(ls,k):
	if len(ls) == 1:
		return ls[0]
	pivot = random.randrange(0,len(ls)-1)
	i = 0
	p = 0
	while p < len(ls):
		if ls[i] <= ls[pivot] and i <= pivot:
			i += 1
		elif ls[i] < ls[pivot] and i > pivot:
			tmp = ls[i]
			del ls[i]
			ls.insert(0,tmp)
			pivot += 1
		elif ls[i] >= ls[pivot] and i >= pivot:
			i += 1
		elif ls[i] > ls[pivot] and i < pivot:
			tmp =ls[i]
			del ls[i]
			ls.append(tmp)
			pivot -= 1
		else:
			i += 1
		p += 1

	if k == pivot +1:
		return ls[pivot]
	elif k < pivot +1:
		return medianOfArray(ls[0:pivot],k)
	else:
		return medianOfArray(ls[pivot+1:],k-pivot-1)

a=[3,4,5,7,1,2,3,5,7,8,10]
print medianOfArray(a,10)
