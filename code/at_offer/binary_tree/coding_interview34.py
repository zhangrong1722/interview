"""
题目：二叉树中和为某一值的路径
     输入一棵二叉树和一个整数 打印出二叉树中节点值的和为输入整数的所有路径 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径
                    10
                /       \
                5       12
            /       \
            4       7
     输入整数22，则打印两条路径：10 5 7和10 12
思路：先序遍历二叉树，用数据保存中间遍历的路径，到叶节点，并且路径和事预期和，则打印路径，注意一个节点搜索完之后，需要将从路径中移除该节点
"""
from binary_tree import BinaryTreeConstrcutor, pre_order


class Solution(object):
    def findPath(self, root, sum):
        if root is None:
            return
        self.helper(root, sum, 0, [])

    def helper(self, root, sum, cur, path):

        if root is not None:
            cur += root.val
            path.append(root.val)
            if cur > sum:
                return
            if root.left is None and root.right is None and cur == sum:
                print(path)
            if root.left is not None:
                self.helper(root.left, sum, cur, path)
            if root.right is not None:
                self.helper(root.right, sum, cur, path)
            path.pop()
            cur -= root.val


s = Solution()

constrcutor = BinaryTreeConstrcutor()
s.findPath(constrcutor(pre=[10, 5, 4, 7, 12], tin=[4, 5, 7, 10, 12]), 22)
s.findPath(constrcutor(pre=[10, 5, 4, 7, 12], tin=[4, 5, 7, 10, 12]), 19)
s.findPath(constrcutor(pre=[10, 5, 4, 7, 12], tin=[4, 5, 7, 10, 12]), 12)
s.findPath(constrcutor([], []), 10)
