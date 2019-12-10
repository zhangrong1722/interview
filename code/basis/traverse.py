class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order_recursion(root):
    if root is not None:
        print(root.val, end=' ')
        pre_order_recursion(root.left)
        pre_order_recursion(root.right)

def in_order_recusion(root):
    if root is not None:
        in_order_recusion(root.left)
        print(root.val, end=' ')
        in_order_recusion(root.right)

def post_order_recusion(root):
    if root is not None:
        post_order_recusion(root.left)
        post_order_recusion(root.right)
        print(root.val, end=' ')

def pre_order_no_recursion(root):
    if root is None:
        return

    stack = list()
    stack.append(root)
    while len(stack):
        cur_node = stack.pop()
        print(cur_node.val, end=' ')
        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)

def in_order_no_recusion(root):
    if root is None:
        return

    stack = list()
    stack.append(root)
    cur_node = root
    while len(stack):
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        node = stack.pop()
        print(node.val, end=' ')
        if node is not None and node.right is not None:
            cur_node = node.right

def post_order_no_recusion1(root):
    if root is None:
        return
    s1, s2 = list(), list()
    s1.append(root)
    while len(s1):
        node = s1.pop()
        s2.append(node.val)
        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)
    return s2[:: -1]

def post_order_no_recusion2(root):
    if root is None:
        return
    s1 = list()
    s1.append(root)
    h, c = None, root
    while len(s1):
        c = s1[-1]
        if c is not None and c.left is not None and h != c.left and h != c.right:
            s1.append(c.left)
        elif c is not None and c.right is not None and h != c.right:
            s1.append(c.right)
        else:
            h = s1.pop()
            print(h.val, end=' ')

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
root.left, root.right = node1, node2
node1.left, node1.right = node3, node4
node2.left = node5

# pre_order_no_recursion(root)
# pre_order_recursion(root)
# in_order_no_recusion(root)
# in_order_recusion(root)
# print(post_order_no_recusion1(root))
post_order_no_recusion2(root)
# post_order_recusion(root)