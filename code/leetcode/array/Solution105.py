# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder)

    def helper(self, pre_start, pre_end, in_start, in_end, pre_order, in_order):
        if pre_start > pre_end or in_start > in_end:
            return None
        root = TreeNode(pre_order[pre_start])
        rootIndex = pre_start
        for i in range(in_start, in_end+1):
            if in_order[i] == pre_order[rootIndex]:
                rootIndex = i
                break
        root.left = self.helper(pre_start+1, pre_start+(rootIndex-in_start), in_start, rootIndex-1, pre_order, in_order)
        root.right = self.helper(pre_start+(rootIndex-in_start)+1, pre_end, rootIndex+1, in_end, pre_order, in_order)
        return root