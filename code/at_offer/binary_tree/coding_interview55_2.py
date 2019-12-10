"""
题目：输入一棵二叉树的根节点 判断该树是不是平衡二叉树 如果某二叉树中任一节点的左右子树的深度相差不超过1 则它就是一棵平衡二叉树
思路：基于coding_interview_55.py脚本内函数 遍历节点 求出任意节点的左右子树的深度 判断其深度之差不超过1 这样算法复杂度为O(n^2) 存在重复遍历
"""
class Solution(object):
    def IsBalancedBinaryTree(self, root):
        if root is None:
            return True
        leftDepth = self.TreeDepth(root.left)
        rightDepth = self.TreeDepth(root.right)
        if abs(leftDepth - rightDepth) <= 1:
            return self.IsBalancedBinaryTree(root.left) and self.IsBalancedBinaryTree(root.right)


    def TreeDepth(self, root):
        if root is None:
            return 0
        return max(root.left, root.right) + 1