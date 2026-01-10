# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def ans(root,target):
            if root is None:
                return False
            if root.left is None and root.right is None:
                return root.val == target
            return ans(root.left,target- root.val) or ans(root.right,target- root.val)
        return ans(root,targetSum)
