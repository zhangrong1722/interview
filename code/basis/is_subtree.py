# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)
    
    def helper(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        
        return s.val == t.val and self.helper(s.left, t.left) and self.helper(s.right, t.right)
    
    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        return s is not None and (self.helper(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))
        