# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None: #same tree
            return True
        if p==None or q==None:   #different size
            return False
        if p.val!=q.val:  #different node
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)