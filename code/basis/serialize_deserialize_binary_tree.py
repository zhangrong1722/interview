class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    """
    先序序列化 反序列化
    """
    def serialize(self, root):
        if root is None:
             return '#'
        else:
            return str(root.val) + '!' + self.serialize(root.left) + '!' + self.serialize(root.right) + '!'

    def deserialize(self, ss):
        if len(ss) == 0:
            return None
        return self.helper(0, ss.split('!'))[0]

    def helper(self, index, values):
        if values[index] == '#':
            return None, index + 1
        root = TreeNode(int(values[index]))
        index += 1
        root.left, index = self.helper(index, values)
        root.right, index = self.helper(index, values)
        return root, index
