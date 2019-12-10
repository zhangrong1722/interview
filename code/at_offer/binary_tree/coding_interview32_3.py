"""
题目三：之字形打印二叉树
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
例如，按之字形打印下图中二叉树的结果为：
 1
 3  2
 4  5  6  7
15 14 13 12 11 10 9 8
                                1
                        /               \
                        2               3
                    /       \       /       \
                   4        5      6         7
                /     \   /   \   / \       /  \
               8      9  10    11 12 13    14   15
我们可以以上面二叉树为例来找解题思路：根节点位于第一层 直接打印 并且依次将其左、右孩子（第二层节点）放入一个容器，因为是先打印3 因此我们可以想到放入栈中 在打印第二层节点时只需出栈即可
打印第三层时 出栈第二层节点是3 因为需要从左到右打印 因此 我们依次将右孩子、左孩子节点放入栈中 注意两个栈是不同的 当第一个栈为空时 就开始出栈第二个栈 然后将出栈元素的子树压入第一个栈
依次类推
"""
from binary_tree import BinaryTreeConstrcutor


class Solution(object):
    def printBinaryTree(self, root):
        if root is None:
            return
        currentNodes, nextNodes = [], []
        currentNodes.append(root)
        layer = 1
        while len(currentNodes) != 0:
            node = currentNodes.pop()
            print(node.val, end=' ')
            # 奇数行
            if layer == 1:
                if node.left is not None:
                    nextNodes.append(node.left)
                if node.right is not None:
                    nextNodes.append(node.right)
            else:
                if node.right is not None:
                    nextNodes.append(node.right)
                if node.left is not None:
                    nextNodes.append(node.left)
            if len(currentNodes) == 0:
                currentNodes = nextNodes.copy()
                nextNodes = []
                layer = 1 - layer
                print('')


s = Solution()
constrcutor = BinaryTreeConstrcutor()
s.printBinaryTree(constrcutor(pre=[1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15],
                              tin=[8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]))
s.printBinaryTree(constrcutor(pre=[1, 2, 3, 4], tin=[4, 3, 2, 1]))
s.printBinaryTree(constrcutor(pre=[1, 2, 3, 4], tin=[1, 2, 3, 4]))
s.printBinaryTree(constrcutor(pre=[], tin=[]))
