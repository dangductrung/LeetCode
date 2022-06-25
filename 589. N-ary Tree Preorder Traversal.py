"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    result = []
    def __init__(self):
        self.result = []
    
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        self.result.append(root.val)
        
        for node in root.children:
            self.preorder(node)
        
        return self.result