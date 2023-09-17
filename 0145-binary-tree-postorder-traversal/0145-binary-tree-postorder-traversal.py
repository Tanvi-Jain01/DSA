# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def traverse(current_node):
            if current_node:
                traverse(current_node.left)
                traverse(current_node.right)
                result.append(current_node.val)

        if root:
            traverse(root)

        return result





        