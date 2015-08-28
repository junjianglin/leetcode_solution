# -*- coding: utf-8 -*-

#-----------------------
#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
#the contiguous subarray [4,−1,2,1] has the largest sum = 6.
#
#-----------------------
def maxiSubArray(ls):
	if len(ls) == 1:
		return ls[0],0,0
	else:
		table = []
		table.append([ls[0],0,0])
		for i in range(1,len(ls)):
			single = ls[i]
			sum_so_far = table[i-1][0]
			start = table[i-1][1]
			end = table[i-1][2]
			new_sum = sum_so_far + sum(ls[end+1:i+1])
			maxValue = max(single,sum_so_far,new_sum)
			#print maxValue,single,sum_so_far,new_sum,end
			if maxValue == single:
				table.append([single,i,i])
			elif maxValue == sum_so_far:
				table.append([sum_so_far,start,end])
			elif maxValue == new_sum:
				table.append([new_sum,start,i])
		return table[len(ls)-1][0],table[len(ls)-1][1]+1,table[len(ls)-1][2]+1

ls = [-2,1,-3,4,-1,2,1,-5,4]
ls2 = [1,-3,5,-2,9,-8,-6,4]
print maxiSubArray(ls)
print maxiSubArray(ls2)
