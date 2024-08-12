'''class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)] * n
        t = list(reversed(s))
        for i in range(n-1 ,-1 ,-1):
            for j in range(n-1 ,-1 ,-1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max( dp[i+1][j] , dp[i][j+1] )
        return dp[0][0]
'''
#a = Solution()
#print(a.longestPalindromeSubseq('bbbdb'))