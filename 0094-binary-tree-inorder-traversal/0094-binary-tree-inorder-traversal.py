# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def traverse(currentnode):
            if currentnode.left:  #recursively call left child
                traverse(currentnode.left)
            result.append(currentnode.val)
            if currentnode.right:
                traverse(currentnode.right)
        if root:
            traverse(root)
        return result
        