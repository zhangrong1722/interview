"""
题目：从上往下打印二叉树
思路：实质上时二叉树的层序遍历
"""
import queue

from binary_tree import BinaryTreeConstrcutor


class Solution(object):
    def printFromTopToBottom(self, root):
        results = []
        if root is None:
            return results

        q = queue.Queue()
        q.put(root)
        while q.qsize() != 0:
            node = q.get()
            results.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return results


s = Solution()
constrcutor = BinaryTreeConstrcutor()
print(s.printFromTopToBottom(constrcutor(pre=[2, 3, 1, 5, 4, 6, 7], tin=[1, 3, 5, 2, 6, 4, 7])))
print(s.printFromTopToBottom(constrcutor(pre=[1, 2, 3, 4], tin=[4, 3, 2, 1])))
print(s.printFromTopToBottom(constrcutor(pre=[1, 2, 3, 4], tin=[1, 2, 3, 4])))
print(s.printFromTopToBottom(constrcutor(pre=[], tin=[])))