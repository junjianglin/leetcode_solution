
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permu_list = []
        a = [0]*len(nums)
        k = -1
        self.backtrack(a,k,nums,permu_list)
        return permu_list
    
    def construct_candidates(self,a,k,input):
        candidates = input[:]
        for i in range(k):
            if a[i] in candidates:
                candidates.remove(a[i])
            i += 1
        return candidates,len(candidates)
    
    def is_a_solution(self,a,k,input):
        if k == len(input)-1:
            return True
        else:
            return False
    def process_solution(self,a,k,input,permu_list):
        b = a[:]
        permu_list.append(b)
    
    def backtrack(self,a,k,input,permu_list):

        if self.is_a_solution(a,k,input):
            self.process_solution(a,k,input,permu_list)
        else:
            k += 1
            c, ncandidates = self.construct_candidates(a,k,input)
            for i in range(ncandidates):
                a[k] = c[i]
                self.backtrack(a,k,input,permu_list)
sol = Solution()
print sol.permute([1,2,3])
