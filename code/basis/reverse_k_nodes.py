class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class KInverse:
    def inverse(self, head, k):
        if head is None:
            return head
        stack, p, newHead = list(), head, ListNode(-1)
        q = newHead

        while p is not None:
            stack.append(p)
            p = p.next
            if len(stack) == k:
                while len(stack) != 0:
                    q.next = stack.pop()
                    q = q.next

        for i in range(len(stack)):
            q.next = stack[i]
            q = q.next

        q.next = None
        return newHead.next

s = KInverse()
node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(2)
node4 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4

# node1 = ListNode(360)
# node2 = ListNode(220)
# node3 = ListNode(2)
# node1.next = node2
# node2.next = node3

s.inverse(node1, 3)
