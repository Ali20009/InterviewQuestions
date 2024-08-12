'''rom collections import defaultdict
class Solution:
    def maximumTotalCost(self, nums):
        results = defaultdict(int)
        res  = 0 
        for i in range(len(nums)):
            res += nums[i] * (-1)** i

        def backtrack(list):
            for j in range(1 , len(list) +1, 2):
                result1 = 0
                result = 0
                for a in range(j):  
                    result1 += list[a] *(-1)** a
                    results[j] = result1
                result = max(result , result1)
                
            highest = max([i for _,i in results.items()])
            return backtrack([nums[k] for k in range(highest , len(nums))])

        return backtrack(nums)'''
'''
class Solution:
    def maximumTotalCost(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i + 1] = max(dp[i] + nums[i], dp[i - 1] + nums[i - 1] - nums[i])
        return dp[n] , dp

'''



# Numpy   Pandas   Matplotlib

class Solution:
    def maximumTotalCost(self ,list1):
        n = len(list1)
        if len(list1) == 1:
            return list1[0]
        
        dp = [0] * (n+1)
        dp[1] = list1[0]
        for i in range(n ):
            dp[i +1] = max(dp[i] + list1[i], dp[i -1] + list1[i -1] - list1[i])
        
        return dp[n ]



a  = Solution()
print(a.maximumTotalCost([1,-2,3,-3,-6,-2]))

