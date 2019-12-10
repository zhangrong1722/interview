from linked_list import Node


class Solution(object):
    def FindFirstCommonNodes(self, head1, head2):
        if head1 is None or head2 is None:
            return None
        # 共同节点为第一个节点
        if head1 == head2:
            return head1
        stack1, stack2 = list(), list()
        p, q = head1, head2
        while p is not None:
            stack1.append(p)
            p = p.next
        while q is not None:
            stack2.append(q)
            q = q.next
        p, q = stack1.pop(), stack2.pop()
        # 公共节点在末尾
        if p == q:
            return p
        while len(stack1) != 0 and len(stack2) != 0:
            p, q = stack1.pop(), stack2.pop()
            if p != q:
                return p.next
        return None

node1, node2, node3, node4, node5, node6, head1 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
# 公共节点在中间
# head2 = Node(8)
# head2.next = node3

# 公共节点在开头
# head2 =head1

# 公共节点在末尾
head2 = Node(8)
head2.next = node5
print(s.FindFirstCommonNodes(head1, head2).val)