#---------------------------
# Problem: Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to buy one share of the stock and sell one share of the stock, design an algorithm to find the best times to buy and sell.
#---------------------------

#Solution : O(n)

def getBestTime(arr):
	if len(arr) == 0:
		print "no best Time"
	i = 1
	miniIndex = 0
	bestValue = 0
	while i < len(arr):
		if arr[i] - arr[miniIndex] > bestValue:
			bestValue = arr[i] - arr[miniIndex]
			bestBuy = miniIndex
			bestSell = i
		if arr[i] < arr[miniIndex] :
			miniIndex = i
		i += 1
	return bestValue,bestBuy,bestSell

#---------------------------
# A following problem: if you can keep buying and selling, 
#how to maximize the profit? for example, if it is 6,1,3,2,4,7, 
#we can buy for 1 and sell for 3, and we can buy for 2, and sell for 4,
#then buy on 4, sell for 7. total maxval =3-1+4-2+7-4 = 7. They would like to have some O(n) solutions.
#---------------------------

def getBestValue(arr):
	if len(arr) == 0:
		print "no best Time"
	i = 1
	miniIndex = 0
	bestValue = 0
	while i < len(arr):
		if arr[i] - arr[miniIndex] > bestValue:
			bestValue = arr[i] - arr[miniIndex]
		if arr[i] < arr[miniIndex] :
			miniIndex = i
		i += 1
	return bestValue


# DP Algorithm
#  P(n) = Max{ P(n-1), P(n-2)+ bestValue[n-1:n], P(n-3)+bestValue[n-2:n], ..., P(1)+bestValue[2:n]}
#
def getBestProfit(arr):
	if len(arr) == 1:
		return 0
	if len(arr) == 2 and arr[1] - arr[0] > 0 :
		return arr[1] - arr[0]
	if len(arr) == 2 and arr[1] <= arr[0]:
		return 0
	ProfitTable = []
	ProfitTable.append(getBestProfit(arr[0:1]))
	ProfitTable.append(getBestProfit(arr[0:2]))

	for i in range(2, len(arr)):
		tmpMax = 0
		for j in range(0,i):
			tmpProfit = ProfitTable[j] + getBestValue(arr[j+1:i+1])
			if  tmpProfit > tmpMax:
				tmpMax = tmpProfit
		ProfitTable.append(tmpMax)
	print ProfitTable
	return ProfitTable[len(ProfitTable)-1]



a=[6,1,3,2,4,7]
print getBestTime(a)
print getBestProfit(a)


