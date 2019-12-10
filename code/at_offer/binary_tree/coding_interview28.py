"""
题目：对称的二叉树
     请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
思路：通常二叉树的遍历有前序、中序和后序 如果一颗二叉树是对称的 则根节点的左子树和右子树是相等的 因此 我们可以自定义一种遍历：右子树->根节点->左子树
     对于对称的二叉树 其先序和我们自定义的二叉树遍历序列必然相等
"""
class Solution(object):
    def isSymmetrical(self, pRoot):
        return self.helper(pRoot, pRoot)

    def helper(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.helper(pRoot1.left, pRoot2.right) and self.helper(pRoot1.right, pRoot2.left)
        return False
