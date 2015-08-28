def mergeSort(ls):
	low = 0
	high = len(ls) - 1
	if low < high:
		middle = (high-low)/2 + 1          # Make a mistake here middle = (high-low)/2
		ls1 = mergeSort(ls[0:middle])
		ls2 = mergeSort(ls[middle:])
		print ls1,ls2
		return merge(ls1,ls2)
	else:
		return ls

def merge(ls1,ls2):
	i=0
	j=0
	ls_new=[]
	while i < len(ls1) and j <len(ls2):
		if ls1[i] < ls2[j]:
			ls_new.append(ls1[i])
			i += 1
		else:
			ls_new.append(ls2[j])
			j += 1
	if i == len(ls1):           # Make a mistake here  i == len(ls1) - 1
		ls_new += ls2[j:]
	else:
		ls_new += ls1[i:]
	return ls_new

a=[4,3,1,6,5,7,8,10,23]
print mergeSort(a)
