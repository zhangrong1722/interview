"""
题目：二叉树的序列化和反序列化
     请实现两个函数，分别用来序列化和反序列化二叉树
"""
from binary_tree import BinaryTreeConstrcutor, TreeNode, pre_order


class Solution:
    def Serialize(self, root):
        if root is None:
            return '$'
        else:
            return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)
    index = 0

    def Deserialize(self, s):
        if s is None or len(s) == 0 or self.index >= len(s):
            return None

        num = s[self.index] if s[self.index] == '$' else int(s[self.index])
        self.index += 2

        if num != '$':
            root = TreeNode(num)
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
            return root
        return None


s = Solution()
# 测试用例一：一般二叉树有
# results = s.Serialize(BinaryTreeConstrcutor()([1, 2, 4, 3, 5, 6], [4, 2, 1, 5, 3, 6]))
# print(results)
# pre_order(s.Deserialize(results))
# print('')

# 测试用例二：完全二叉树
# results = s.Serialize(BinaryTreeConstrcutor()([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]))
# print(results)
# pre_order(s.Deserialize(results))

# 测试用例三：所有节点均只有左子树
# results = s.Serialize(BinaryTreeConstrcutor()([1, 2, 3, 4], [4, 3, 2, 1]))
# print(results)
# pre_order(s.Deserialize(results))

# 测试用例四：所有节点均只有右子树
# results = s.Serialize(BinaryTreeConstrcutor()([1, 2, 3, 4], [1, 2, 3, 4]))
# print(results)
# pre_order(s.Deserialize(results))

# 测试用例五：空树
# print(s.Serialize(None))
# s.Deserialize(None)