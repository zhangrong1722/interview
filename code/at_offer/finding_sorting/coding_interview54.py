"""
面试题目：二叉搜索树的第k大节点
        给定一棵二叉搜索树 请找出其中第k大的节点。例如：
                             5
                            / \
                           3   7
                          / \ / \
                          2 4 6 8
        按照节点大小顺序 第三大节点的值是4
思路：这道题目思路比较简单 二叉搜索树的中序序列就是一个递增序列 因此只需要遍历中序序列 然后返回第k大的节点即可
"""
class Solution(object):
    def FindKNodeInBinarySearchTree(self, root, k):
        if root is None or k < 0:
            return None
        p, stack1 = root, list()
        while p is not None or len(stack1) != 0:
            if p is not None:
                stack1.append(p)
                p = p.left
            if len(stack1) != 0:
                node = stack1.pop()
                k -= 1
                if k == 0:
                    return node

                p = node.right
        return None
