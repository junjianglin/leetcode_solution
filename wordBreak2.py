class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        l = len(s)
        dp = [[] for i in range(l)]
        if s[0] in dict:
            dp[0].append(s[0])
        for i in range(1,l):
            if s[0:i+1] in dict:
                dp[i].append(s[0:i+1])
            for j in range(0,i):
                if dp[j] != []:
                    if s[j+1:i+1] in dict:
                        for x in dp[j]:
                            dp[i].append(x+" "+s[j+1:i+1])
        return dp[l-1]

a = Solution()
s = "catsanddog"
s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
s3 = "aaaaaaa"
dict = ["cat", "cats", "and", "sand", "dog"]
dict2 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
dict3 = ["aaaa","aa","a"]
print a.wordBreak(s3,dict3)