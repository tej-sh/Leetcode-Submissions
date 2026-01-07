# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def totalsum(root):
            if root is None:
                return 0
            return root.val+totalsum(root.left)+totalsum(root.right)
        
        totsum = totalsum(root)
        
        
        def halfsum(root):
            nonlocal mx
            if root is None:
                return 0
            l = halfsum(root.left)
            r = halfsum(root.right)
            half = l+r+root.val
            mx = max(mx,(totsum-half)*half)
            return half
        mx = 0
        halfsum(root)
        return mx%((10**9)+7)

        
        
