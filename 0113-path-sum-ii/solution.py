# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        def ans(root,cur):
            if root is None:
                return 
            cur.append(root.val)
            if root.left is None and root.right is None and targetSum == sum(cur):
                res.append(cur[::])
            ans(root.left,cur)
            ans(root.right,cur)
            cur.pop()
        ans(root,[])
        return res
