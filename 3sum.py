class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        l = len(num)
        if l < 3:
            return []
        result = []
        num.sort()
        for i in range(l-2):
            if i>0 and num[i] == num[i-1]:
                continue
            target = 0-num[i]
            low = i+1
            high = l-1
            while low < high:
                if num[low]+num[high] < target:
                    low += 1
                    while num[low] == num[low-1] and low<high:
                        low += 1
                elif num[low]+num[high] > target:
                    high -= 1
                    while num[high] == num[high+1] and low<high:
                        high -= 1
                else:
                    result.append([num[i],num[low],num[high]])
                    low += 1
                    while num[low] == num[low-1] and low<high:
                        low += 1
                    high -= 1
                    while num[high] == num[high+1] and low<high:
                        high -= 1
        return result

a=Solution()
num = [-2,-7,-11,-8,9,-7,-8,-15,10,4,3,9,8,11,1,12,-6,-14,-2,-1,-7,-13,-11,-15,11,-2,7,-4,12,7,-3,-5,7,-7,3,2,1,10,2,-12,-1,12,12,-8,9,-9,11,10,14,-6,-6,-8,-3,-2,14,-15,3,-2,-4,1,-9,8,11,5,-14,-1,14,-6,-14,2,-2,-8,-9,-13,0,7,-7,-4,2,-8,-2,11,-9,2,-13,-10,2,5,4,13,13,2,-1,10,14,-8,-14,14,2,10]
num1 = [-2,0,1,1,2]
print a.threeSum(num1)