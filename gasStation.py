class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        lgas = len(gas)
        lcost = len(cost)
        if lgas == 0 or lcost == 0:
            return -1
        if lgas == 1 and lcost == 1 and gas[0]>=cost[0]:
            return 0
        curGas = 0
        for i in range(lgas):
            curGas = gas[i]
            curPos = i
            while curGas >= cost[curPos]:
                curPos += 1
                if curPos == lgas:
                    curPos = 0
                    if i == 0:
                        return i
                    curGas = curGas-cost[-1]+gas[curPos]
                elif curPos == i:
                    return i
                else:
                    curGas = curGas-cost[curPos-1]+gas[curPos]
        return -1
        

a = Solution()

gas1 = [x for x in range(4000,0,-1)]
cost1 = [x for x in range(1,4001,1)]
gas2 = [2,1]
cost2 = [1,2]
print a.canCompleteCircuit(gas1,cost1)
