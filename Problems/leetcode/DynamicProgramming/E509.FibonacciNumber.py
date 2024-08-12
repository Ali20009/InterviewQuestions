class Solution:
    def fib(self , n :int) -> int:
        ##0 1 1 2 3 5 8 13 21 ...
        ans = {0: 0,1:1}
        dp = [0] * (n+1)
        if n in ans :
            return ans[n]
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
a = Solution()
print(a.fib(0))