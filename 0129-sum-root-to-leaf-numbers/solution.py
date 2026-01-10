# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def ans(root,cur):
            nonlocal s
            if root is None:
                return
            cur += str(root.val)
            if root.left is None and root.right is None:
                s += int(cur[:])
            ans(root.left,cur)
            ans(root.right,cur)
            cur[:-1]
        ans(root,"")
        return s
