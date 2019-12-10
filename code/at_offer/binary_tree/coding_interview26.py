"""
题目：输入两棵二叉树A和B，判断B是不是A的子结构。
思路：先遍历A树，在A树中找到与B树根节点相同的节点，再从该节点开始依次比较两棵子树节点是否相等；如果相等，则是子树，返回True；否则，继续遍历A
     树，在A树中查找与B树根节点相等的节点；例如：
                8                               8
             /      \                       /       \
             8       7                      9        2
          /     \
         9       2
              /     \
             4       7
     显然，B树是A树的子结构
"""
from binary_tree import BinaryTreeConstrcutor


class Solution(object):
    def isSubTree(self, root1, root2):
        if root1 is None or root2 is None:
            return False
        results = False
        if root1.val == root2.val:
            results = self.helper(root1, root2)
        if not results:
            results = self.isSubTree(root1.left, root2)
        if not results:
            results = self.isSubTree(root1.right, root2)
        return results

    def helper(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.left) and self.helper(root1.right, root2.right)


s = Solution()
constrcutor = BinaryTreeConstrcutor()
print(s.isSubTree(constrcutor(pre=[1, 8, 9, 2, 4, 6, 7], tin=[9, 8, 4, 2, 6, 1, 7]),
                  constrcutor(pre=[8, 9, 2], tin=[9, 8, 2])))
print(s.isSubTree(constrcutor(pre=[1, 8, 9, 2, 4, 6, 7], tin=[9, 8, 4, 2, 6, 1, 7]),
                  constrcutor(pre=[8, 7, 2], tin=[7, 8, 2])))
print(s.isSubTree(constrcutor(pre=[1], tin=[1]), constrcutor(pre=[1], tin=[1])))
print(s.isSubTree(constrcutor(pre=[], tin=[]), constrcutor(pre=[1], tin=[1])))
print(s.isSubTree(constrcutor(pre=[], tin=[]), constrcutor(pre=[], tin=[])))
