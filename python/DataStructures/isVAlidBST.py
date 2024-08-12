import math
from queue import LifoQueue as Stack 
#print(math.log2(8))
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        
        
        def isvalid(node, min, max):
            if not node:
                return True
            if node.val > max or node.val < min:
                return False
            
            return isvalid(node.left, min, node.val) and isvalid(node.right, node.val, max)
        return isvalid(root, float('-inf'), float('inf'))


class Solution2:
    def ValidBST(self, root):
        stack = Stack()
        pre = 0
        while root or not stack.empty():
            while root:
                stack.put(root)
                root  =root.left
            
            root = stack.get()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True
        

        


a = Solution()
a.isValidBST([1,2,3])

# [5,1,4,null,null,3,6]