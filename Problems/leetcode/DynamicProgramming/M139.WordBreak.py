class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n , -1 ,-1):
            if dp[i] == True:
                for j in wordDict:
                    if s[i-len(j):i] == j:
                        dp[i-len(j)] = True
               
        return  dp[0]
     
a = Solution()
print(a.wordBreak(s = "leetcode", wordDict = ["leet","code"]))

'''class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        for i in range(len(s) -1 , -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[ i + len(word)]
                if dp[i]:
                    break
        return dp[0]'''