# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def traversal(node, level):
            if node == None:
                return None
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            
            traversal(node.left, level + 1)
            traversal(node.right, level + 1)
            
        traversal(root, 0)
        return res