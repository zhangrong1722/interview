class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def trasver(root):
    while root is not None:
        print(root.val)
        root = root.next

class Palindrome:
    def isPalindrome(self, pHead):
        if pHead is None or pHead.next is None:
            return True
        p, q, stack = pHead, pHead.next, list()
        
        while q is not None and q.next is not None:
            stack.append(p.val)
            p, q = p.next, q.next.next
        q, n = pHead, 0
        while q is not None:
            n, q = n+1, q.next

        end_node = pHead
        if n % 2 == 0:
            while end_node != p:
                end_node = end_node.next
        else:
            while end_node.next != p:
                end_node = end_node.next

        p = p.next
        q = None
        t = pHead
        temp = None
        while t != end_node:
            temp = t
            t = t.next
            if q is None:
                q = temp
                temp.next = None
            else:
                temp.next = q
                q = temp

        t.next = q
        q = t
        trasver(q)

        while p is not None:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Palindrome()
print(s.isPalindrome(node1))