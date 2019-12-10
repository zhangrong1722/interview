"""
题目：链表中环的入口节点
     如果一个链表中包含环，如何找出环的入口节点？例如，1->2->3->4->5->6->3
思路：使用双指针p、q；p指针走一步，q指针一次走两步；在p指针为空之前，如果q没有追上p，表明链表中没环，否则，有环；
     如果有环，下一步找链表中环的入口节点，依旧使用双指针p和q，设环中有k个节点，让p先走k步，接下来让p和q同时每次只走一步，
     当p再次相遇时，相遇节点便是入口节点；
"""
from linked_list import Node, build


class Solution(object):
    def findEntrance(self, header):
        # 空链表或者只有一个节点
        if header is None or header.next is None:
            return None
        hasCricle = False
        p, q = header, header.next
        while q is not None and p.next.next is not None:
            if p == q:
                hasCricle = True
                break
            p, q = p.next.next, q.next
        if hasCricle:
            counts = self.nodesCountInCricle(p)
            p, q = header, header
            for i in range(counts):
                p = p.next
            while p is not None and q is not None and p != q:
                p, q = p.next, q.next
            return p
        else:
            return None

    def nodesCountInCricle(self, p):
        q = p.next
        counts = 1
        while q is not None and p != q:
            counts += 1
            q = q.next
        return counts

header = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)
header.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

s = Solution()
# 有环
print(s.findEntrance(header).val)
# 无环的单链表
print(s.findEntrance(build([1, 2, 3, 4, 5])))
# 只有一个节点
print(s.findEntrance(build([1])))
# 空链表
print(s.findEntrance(None))