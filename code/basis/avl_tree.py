class Solution(object):
    def definition(self, root):
        if root is None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.definition(root.left) and self.definition(root.right)
        else:
            return False

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

class Solution(object):
    is_balanced = True
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        self.getHeight(pRoot, 1)
        return self.is_balanced
    
    def getHeight(self, pRoot, level):
        if pRoot is None:
            return level + 1
        left_height = self.getHeight(pRoot.left, level + 1)
        if not self.is_balanced:
            return left_height
        right_height = self.getHeight(pRoot.right, level + 1)
        if abs(left_height - right_height) > 1:
            self.is_balanced = False
        return max(left_height, right_height)