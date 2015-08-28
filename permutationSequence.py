

import math
class Solution:
    # @return a string
    """
    #This one is TLE for 8,15485
    def getPermutation(self, n, k):
        if n == 1 and k == 1:
            return 1
        ls = self.helper(n)
        ls = sorted(ls)
        return ls[k-1]
    
    def helper(self,n):
        map = []
        map.append(['1'])
        for i in range(2,n+1):
            map.append([])
            for x in map[i-2]:
                k = 0
                while k <= len(x):
                    map[i-1].append(x[0:k]+str(i)+x[k:])
                    k += 1
            
            i += 1
        return map[n-1]
    """
    """
    #This one works fine
    def getPermutation(self, n, k):
        if n == 1 and k == 1:
            return str(1)
        ls = range(1,n+1)
        result = ''
        return result + self.helper(ls,k)
    
    def helper(self,ls,k):
        l = len(ls)
        if l == 1:
            return str(ls[0])
        if k%math.factorial(l-1) == 0:
            digit = str(ls[(k/(math.factorial(l-1)))-1])
            del ls[(k/math.factorial(l-1))-1]
            return digit + self.helper(ls,k - ((k/math.factorial(l-1))-1)*math.factorial(l-1))
        else:
            digit = str(ls[(k/(math.factorial(l-1)))])
            del ls[(k/math.factorial(l-1))]
            return digit + self.helper(ls,k % math.factorial(l-1))
    """
    #Best
    def getPermutation(self, n, k):
    array = range(1, n + 1)
    k = (k % math.factorial(n)) - 1
    permutation = []
    for i in xrange(n - 1, -1, -1):
        idx, k = divmod(k, math.factorial(i))
        permutation.append(array.pop(idx))

    return "".join(map(str, permutation))



a = Solution()
print a.getPermutation(8,15485)