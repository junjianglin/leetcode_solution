class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        l = len(A)
        if l <= 2:
            return l
        new_l = 1
        t = 1
        for i in range(1,l):
            if A[new_l-1] == A[i]:
                t += 1
                if t <= 2:
                    A[new_l] = A[i]
                    new_l += 1
            else:
                t = 1
                A[new_l] = A[i]
                new_l += 1

a = Solution()
t1 = [1,1,1]
