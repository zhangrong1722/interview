class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    """
    该问题可分三种情况，并结合下面例子进行说明：
                    a
                   / \
                  b   c
                 / \ / \
                d  e f  g
                  / \
                  h j
    考虑到中序遍历的顺序是左-中-右，任一节点的下一节点一定不会出现在其左子树中，只会出现在其右子树或者向上父节点中
    因此，我们首先考虑节点有右子树的情况，在这种情况下，下一节点一定是其右子树的最左边节点，例如b节点的下一节点是h
    如果节点没有右子树，我们还需要考虑到该节点是否是其父节点的左孩子节点，如果是，下一节点节点是其父节点，例如d节点的下一节点是其父节点b
    如果该节点没有右子树，但不是其父节点的左孩子节点，比如j节点，这种情况就比较复杂了，我们需要沿着该节点一直往上找，直到找到一个左孩子节点，
    那么该左孩子节点的父节点便是下一节点，比如j节点，我们往上找到b节点，其父节点是j节点的下一节点
    """
    def GetNext(self, pNode):
        if pNode is None:
            # 空树
            return None

        if pNode.right is not None:
            # 有右子树
            temp = pNode.right
            while temp.left is not None:
                temp = temp.left
            return temp
        elif pNode.right is None and pNode.next is not None and pNode.next.left == pNode:
            # 没有右子树 该节点是父节点的左孩子节点
            return pNode.next
        elif pNode.right is None and pNode.next is not None and pNode.next.left != pNode:
            # 没有右子树 该节点也不是父节点的左孩子节点（即右孩子节点）
            temp = pNode
            while True:
                if temp.next is None:
                    return None
                if temp.next.left == temp:
                    return temp.next
                temp = temp.next

        return None
