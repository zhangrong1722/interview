"""
题目：分行从上到下打印二叉树
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。例如，打印图4.7中二叉树的结果为：
8
6 10
5  7 9 11
                                            8
                                        /       \
                                       6         10
                                    /      \    /   \
                                    5       7  9    11
思路：从上到下分行打印二叉树 本质上还是层序遍历二叉树 为了达到按层遍历二叉树的目的 我们需要额外两个变量 一个变量存储当前剩余的节点数 另一变量
     存储下一层的节点数
"""
import queue

from binary_tree import BinaryTreeConstrcutor


class Solution(object):
    def printBinaryTreeByRows(self, root):
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        currentNodes, nextNodes = 1, 0
        while q.qsize() != 0:
            node = q.get()
            print(node.val, end=' ')
            currentNodes -= 1
            if node.left is not None:
                q.put(node.left)
                nextNodes += 1
            if node.right is not None:
                q.put(node.right)
                nextNodes += 1
            if currentNodes == 0:
                print('')
                currentNodes = nextNodes
                nextNodes = 0


s = Solution()
constrcutor = BinaryTreeConstrcutor()
s.printBinaryTreeByRows(constrcutor(pre=[8, 6, 5, 7, 10, 9, 11], tin=[5, 6, 7, 8, 9, 10, 11]))
s.printBinaryTreeByRows(constrcutor(pre=[1, 2, 3, 4], tin=[4, 3, 2, 1]))
s.printBinaryTreeByRows(constrcutor(pre=[1, 2, 3, 4], tin=[1, 2, 3, 4]))
s.printBinaryTreeByRows(constrcutor(pre=[], tin=[]))
