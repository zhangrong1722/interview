# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        This code is based on the following fact:
        Being pre-order can be divided into three parts:[root,left subtree, right subtree].
        Being in-order can be divided into three parts:[left subtree,root,right subtree].
        Being post-order can be divided into three parts:[left subtree,right subtree,root].
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(inorder)-1, 0, len(postorder)-1, inorder, postorder)

    def helper(self, in_start, in_end, post_start, post_end, in_order, post_order):
        if in_start > in_end or post_start > post_end:
            return None
        root = TreeNode(post_order[post_end])
        rootIndex = post_end
        for i in range(in_start, in_end+1):
            if in_order[i] == post_order[rootIndex]:
                rootIndex = i
                break

        root.left = self.helper(in_start, rootIndex-1, post_start, post_start+rootIndex-in_start-1, in_order, post_order)
        root.right = self.helper(rootIndex+1, in_end, post_start+rootIndex-in_start, post_end-1, in_order, post_order)
        return root

