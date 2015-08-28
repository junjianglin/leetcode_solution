#---------------------
#    overlap rectangle problem:
#  Given two axis-aligned rectangles A and B. Write a function to determine if the two rectangles overlap.
#---------------------

def rectangleOverlap(ls1,ls2):
	if ls1[1][1] > ls2[0][1] or ls1[1][0] < ls2[0][0] or ls1[0][0] > ls2[1][0] or ls1[0][1] < ls2[1][1]:
		return False
	else:
		return True

ls1=[(1,4),(5,2)]
ls2=[(4,3),(7,0)]
ls3 = [(7,1),(9,0)]

print rectangleOverlap(ls1,ls2)
print rectangleOverlap(ls1,ls3)
