# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        else:
            return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None, ]
        all_trees = []
        for root in range(start, end+1):
            left_nodes = self.helper(start, root-1)
            right_nodes = self.helper(root + 1, end)
            for l in left_nodes:
                for r in right_nodes:
                    root_node = TreeNode(root)
                    root_node.left=l
                    root_node.right=r
                    all_trees.append(root_node)
        return all_trees
