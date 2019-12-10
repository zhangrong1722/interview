from binary_tree import TreeNode, pre_order


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        return self.constrcut(pre, tin, 0, len(pre) - 1, 0, len(tin) - 1)

    def constrcut(self, pre, tin, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        rootIndex = 0
        for i in range(inStart, inEnd + 1):
            if pre[preStart] == tin[i]:
                rootIndex = i
                break
        root = TreeNode(pre[preStart])
        root.left = self.constrcut(pre, tin, preStart + 1, preStart + rootIndex - inStart, inStart, rootIndex - 1)
        root.right = self.constrcut(pre, tin, preStart + rootIndex - inStart + 1, preEnd, rootIndex + 1, inEnd)
        return root

s = Solution()
pre_order(s.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6]))