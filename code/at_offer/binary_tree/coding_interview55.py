"""
题目：二叉树的深度
思路：设一个节点的左子树的深度为m 右子树的深度为n 则以该节点为根节点的树的深度=max(m+n)+1
"""
class Solution(object):
    def TreeDepth(self, root):
        if  root is None:
            return 0
        return max(self.TreeDepth(root.left), self.TreeDepth(root.right)) + 1