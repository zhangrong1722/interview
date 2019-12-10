class TreeNode(object):
    """
    二叉树节点
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    """
    前序遍历二叉树
    """
    if root is None:
        return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """
    中序遍历二叉树
    """
    if root is None:
        return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)


def post_order(root):
    """
    后序遍历二叉树
    """
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')


def in_order_no_recursion(root):
    """
    借用栈中序遍历非递归
    """
    if root is None:
        return
    p, stack1 = root, list()
    while p is not None or len(stack1) != 0:
        while p is not None:
            stack1.append(p)
            p = p.left

        if len(stack1) != 0:
            # 访问根节点
            node = stack1.pop()
            print(node.val, end=' ')
            p = node.right


def pre_order_no_recursion(root):
    """
    借用栈前序遍历非递归
                5
               / \
              3  4
             /\   \
            1  2   7
    """
    if root is None:
        return
    p, stack1 = root, list()
    while p is not None or len(stack1) != 0:
        while p is not None:
            print(p.val, end=' ')
            stack1.append(p)
            p = p.left
        if len(stack1) != 0:
            node = stack1.pop()
            p = node.right


class BinaryTreeConstrcutor:
    """
    根据先序和中序序列新建二叉树
    """
    def __call__(self, pre, tin):
        if pre is None or tin is None or len(pre) != len(tin) or len(pre) == 0 or len(pre) != len(set(pre)):
            return None
        return self.helper(pre, tin, 0, len(pre) - 1, 0, len(tin) - 1)

    def helper(self, pre, tin, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd:
            return None
        rootIndex = 0
        for i in range(inStart, inEnd + 1):
            if pre[preStart] == tin[i]:
                rootIndex = i
                break
        root = TreeNode(pre[preStart])
        root.left = self.helper(pre, tin, preStart + 1, preStart + rootIndex - inStart, inStart, rootIndex - 1)
        root.right = self.helper(pre, tin, preStart + rootIndex - inStart + 1, preEnd, rootIndex + 1, inEnd)
        return root


root = BinaryTreeConstrcutor()(pre=[5, 3, 1, 2, 4, 7], tin=[1, 3, 2, 5, 4, 7])
pre_order_no_recursion(root)
print('')
in_order_no_recursion(root)