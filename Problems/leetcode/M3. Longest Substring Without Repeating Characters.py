from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
    
        q = deque()

        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            res = max(res, len(q))

        return res 


'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = dict()
        length = 0
        while s[length] not in seen.keys():
            seen[s[length]] = length + 1
            length += 1
            if length == len(s) :
                return length
    
    
        return max(self.lengthOfLongestSubstring(s[seen[s[length]]:]) , length)


A = Solution()
print(A.lengthOfLongestSubstring("dvdf"))
    
'''
