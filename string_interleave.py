class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
        if s3 == "":
            return False
        q = collections.deque()
        v = set()
        q.append((0,0,0))
        v.add((0,0,0))
        
        while q:
            head = q.popleft()
            i,j,k = head
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if i < len(s1) and k< len(s3) and s1[i] == s3[k]:
                if (i+1,j,k+1) not in v:
                    q.append((i+1,j,k+1))
                    v.add((i+1,j,k+1))
            if j < len(s2) and k< len(s3) and s2[j] == s3[k]:
                if (i,j+1,k+1) not in v:
                    q.append((i,j+1,k+1))
                    v.add((i,j+1,k+1))
        return False



s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
a = Solution()
a.isInterleave(s1,s2,s3)