
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums) -1
        change = True
        for i in range(n, 0, -1):
            if nums[i] > nums[i - 1]:
                temp = nums[i-1]
                while nums[i - 1] >= nums[n]:
                    n -= 1
                nums[i - 1] = nums[n]
                nums[n] = temp
                change = False
                nums[i:] = sorted(nums[i:])
                break
        if change:
            nums[:] = list(reversed(nums))
        return nums
        
a = Solution()
print(a.nextPermutation([1,5,1]))


'''

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        change = True
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i - 1]:
                temp = nums[i-1]
                while nums[i - 1] >= nums[n-1]:
                    n -= 1
                nums[i - 1] = nums[n-1]
                nums[n-1] = temp
                change = False
                nums[i:] = sorted(nums[i:])
                break
        if change:
            nums[:] = list(reversed(nums))
        return nums
        
'''