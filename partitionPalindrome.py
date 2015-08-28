class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        l = len(s)
        if l == 0:
            return []
        dp = [[] for i in range(l)]
        dp[0].append([w for w in s])
        for i in range(l,0,-1):
                for part in dp[l-i]:
                    for j in range(i-1):
                        tmp = part[j]+part[j+1]
                        tmpP = part[0:j]+[tmp]+part[j+2:]
                        if  tmpP not in dp[l-i+1] and self.checkPalin(tmp):
                            dp[l-i+1].append(tmpP)
                    for j in range(i-2):
                        tmp = part[j]+part[j+1]+part[j+2]
                        tmpP = part[:j]+[tmp]+part[j+3:]
                        if tmpP not in dp[l-i+2] and self.checkPalin(tmp):
                            dp[l-i+2].append(tmpP)
        result = []
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                result.append(dp[i][j])
        print dp
        return result
        
    def checkPalin(self,s):
        mid = len(s)/2
        for i in range(mid+1):
            if s[i] != s[-(i+1)]:
                return False
        return True

a = Solution()
s = "abcdefgadslfjadlsfkjl"
#print a.checkPalin('an')
print a.partition(s)