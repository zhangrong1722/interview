class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def trasver(root):
    while root is not None:
        print(root.val)
        root = root.next

class Divide:
    def listDivide(self, head, val):
        if head is None:
            return head
        left, right, middle = ListNode(-1), ListNode(-1), ListNode(-1)
        p, q, r = left, right, middle
        
        t = head
        while t is not None:
            if t.val == val:
                r.next = t
                r = r.next
            elif t.val > val:
                q.next = t
                q = q.next
            else:
                p.next = t
                p = p.next
            t = t.next


        p.next, q.next, r.next = None, None, None
        r.next = right.next
        p.next = middle.next
        return left.next

s = Divide()
# node1 = ListNode(1)
# node2 = ListNode(4)
# node3 = ListNode(2)
# node4 = ListNode(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4

node1 = ListNode(360)
node2 = ListNode(220)
node3 = ListNode(2)
node1.next = node2
node2.next = node3

s.listDivide(node1, 2)
