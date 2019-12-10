"""
题目：从尾到头打印链表
输入一个链表的头结点，从尾到头打印出每个元素的值。
"""
from linked_list import Stack, build


class Solution(object):
    def by_stack(self, header):
        """
        首先肯定要遍历链表，此时我们肯定要遍历链表，但是输出确实逆序的，因而我们可利用栈来实现这一功能。
        """
        s = Stack()
        while header is not None:
            s.push(header.val)
            header = header.next
        while not s.is_empty():
            print(s.pop())

    def by_recursion(self, header):
        """
        上面既然说到用栈来实现功能，另外一种方式自然是递归
        :return:
        """
        if header.next is not None:
            self.by_recursion(header.next)
        print(header.val)

    def build_new(self, header):
        """
        可先遍历链表，同时再利用头插法新建一个链表，再遍历新链表即可。
        """
        pass

s = Solution()
# header = build([1, 2, 3, 4, 5])
header = build([1])

s.by_stack(header)

s.by_recursion(header)