from statistics import  median , mean
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return mean(nums1+nums2)
    
a = Solution()
print(a.findMedianSortedArrays([1,2],  [3,4]))