"""
题目：二叉搜索树的后序遍历序列
     输入一个整数数组，判断该数组是不是某二叉搜索树的后续遍历结果。如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
     例如，输入数组{5,7,6,9,11,10,8}，则返回true；输入数组{7,4,6,5}，则返回false；
思路：数组{5,7,6,9,11,10,8}，最后一个节点8是根节点，根据二叉搜索树的定义，{5, 7, 6}是左子树，{9,11,10}是右子树；我们再看序列{5, 7, 6}，
     最后一个节点6是根节点，5是其左子树，7是右子树，符合二叉搜索树定义；同理，{9,11,10}也符合二叉搜索树定义；
     数组{7,4,6,5}，最后一个节点5是根节点，7>5，因此{7,4,6}是其右子树；但是4<5，因而不符合二叉搜索树定义，返回false；
"""


class Solution(object):
    def isPostOrderOfSearchTree(self, sequence):
        if sequence is None or len(sequence) == 0:
            return False
        return self.helper(sequence, 0, len(sequence) - 1)

    def helper(self, sequence, start, end):
        root = sequence[-1]
        i = start
        # 找左子树 {5,7,6,9,11,10,8}
        for i in range(start, end):
            if sequence[i] > root:
                break
        for j in range(i + 1, end):
            # 如果右子树存在比根节点小的节点 则直接返回false
            if sequence[j] < root:
                return False

        left = True
        # 如果左子树节点少于两个，则直接返回True
        if i - start > 1:
            left = self.helper(sequence, start, i - 1)

        right = True
        # 如果右子树节点少于两个，则直接返回True
        if end - i > 1:
            right = self.helper(sequence, i, end - 1)
        return left and right


s = Solution()
print(s.isPostOrderOfSearchTree([5, 7, 6, 9, 11, 10, 8]))
print(s.isPostOrderOfSearchTree([7, 4, 6, 5]))
print(s.isPostOrderOfSearchTree([5, 6, 7, 8]))
print(s.isPostOrderOfSearchTree([8, 7, 6, 5]))
print(s.isPostOrderOfSearchTree([]))
print(s.isPostOrderOfSearchTree(None))
