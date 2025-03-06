# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(root,l1):
            if root is None:
                return l1
            inorder(root.left,l1)
            l1.append(root.val)
            inorder(root.right,l1)
        
        res =[]
        inorder(root,res)
        return res
