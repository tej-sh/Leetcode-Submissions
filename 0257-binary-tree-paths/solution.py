# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def ans(root,path):
            if root is None:
                return
            if path =="":
                path += str(root.val)
            else:
                path += "->"+str(root.val)
            if root.left is None and root.right is None:
                res.append(path)
            ans(root.left,path)
            ans(root.right,path)
        ans(root,"")
        return res
