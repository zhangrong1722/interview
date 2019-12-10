"""
题目：镜像二叉树
     请完成一个函数，输入一个二叉树，该函数输出它的镜像。例如：
                8
            /       \
           6         10
        /      \    /   \
       5        7  9    11

                8
            /       \
           10         6
        /      \    /   \
       11        9  7    5

思路：粗一看 这一题还是挺难的 但是仔细一看 比方说在根节点 我们只需要互换左孩子和右孩子指针指向 便可达到10和6的镜像
     同样的互换操作可递归应用到其孩子节点，直到其叶子节点；
"""


class Solution(object):
    def Mirror(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left is not None:
            self.Mirror(root.left)
        if root.right is not None:
            self.Mirror(root.right)
