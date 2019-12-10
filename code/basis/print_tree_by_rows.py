import queue

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def print_tree(self, root):
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.val, end=' ')
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def print_tree_by_rows(self, root):
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        cur_last, next_last = root, root
        res, temp = list(), list()
        while not q.empty():
            node = q.get()
            temp.append(node.val)
            
            if node.left is not None:
                next_last = node.left
                q.put(node.left)

            if node.right is not None:
                next_last = node.right
                q.put(node.right)

            if cur_last == node:
                res.append(temp[:])
                temp.clear()
                cur_last = next_last
        return res

s = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
root.left, root.right = node1, node2
node1.left, node1.right = node3, node4
node2.left = node5


print(s.print_tree_by_rows(root))
