"""
题目：合并两个排序的链表
     输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的；
"""
from linked_list import build, traverse


class Solution(object):
    def mergerLinkedList(self, header1, header2):
        if header1 is None:
            return header2
        if header2 is None:
            return header1
        p, q, r, t, newHeader = header1, header2, None, None, None

        while p is not None and q is not None:
            if p.val < q.val:
                if newHeader is None:
                    newHeader = p
                    t = newHeader
                else:
                    t.next = p
                    t = t.next
                p = p.next
            else:
                if newHeader is None:
                    newHeader = q
                    t = newHeader
                else:
                    t.next = q
                    t = t.next
                q = q.next
        while p is not None:
            t.next = p
            p, t = p.next, t.next
        while q is not None:
            t.next = q
            q, t = q.next, t.next
        t.next = None
        return newHeader

s = Solution()
traverse(s.mergerLinkedList(build([1, 3, 5, 7]), build([2, 4, 6, 8])))
traverse(s.mergerLinkedList(build([1, 3, 5, 7, 7]), build([1, 3, 3, 5, 8])))
traverse(s.mergerLinkedList(build([1]), build([2])))
traverse(s.mergerLinkedList(build([]), build([])))
