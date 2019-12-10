"""
题目：反转链表;定义一个函数，输入一个链表的头结点，反转该链表并输出反转后的头结点
思路：假设链表为1->2->3->4->5：当链表为空或者只有一个节点时，直接返回，不做任何处理；当链表节点数多余1个时，用以下解法；
     设遍历到p节点时，q指向p的下一节点；将q指向p，再将q的下一节点存为r节点，此时只需要将p和q节点往后移动一位即可；
"""
from linked_list import build, traverse


class Solution(object):
    def reverseLinkedList(self, header):
        if header is None or header.next is None:
            return header
        p, q, r = header, header.next, None
        header.next = None
        while q is not None:
            r = q.next
            q.next = p
            p = q
            q = r
        header = p
        return header

s = Solution()
print(traverse(s.reverseLinkedList(build([1, 2, 3, 4, 5]))))
print(traverse(s.reverseLinkedList(build([]))))
print(traverse(s.reverseLinkedList(build([1]))))