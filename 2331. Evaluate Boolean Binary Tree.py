# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> bool:
            if node.val == 0 or node.val == 1:
                return node.val == 1
            
            if node.val == 2:
                return check(node.left) | check(node.right)
            
            if node.val == 3:
                return check(node.left) & check(node.right)
            
            
        return check(root)
            