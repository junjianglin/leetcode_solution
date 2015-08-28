class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        low = 1
        high = x-1
        while True:
            mid = (low+high)/2
            if low > high:
                break
            if mid*mid <= x and (mid+1)**2 > x:
                return mid
            elif mid*mid < x and (mid+1)**2 <= x:
                low = mid+1
            elif mid*mid > x and (mid+1)**2 > x:
                high = mid -1

a = Solution()
print a.sqrt(9)