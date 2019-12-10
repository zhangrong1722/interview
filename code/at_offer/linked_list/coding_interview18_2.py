"""
题目：删除链表中重复的节点。例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：双指针，设双指针为pre，post；注意pre的下一节点始终是post
"""
from linked_list import build, traverse


class Solution(object):
    def deleteeduplicativeNodes(self, header):
        # 如果是空或者只有一个节点，直接退出
        if header is None or header.next is None:
            return header
        pre, post = header, header.next
        while post is not None:
            if pre.val == post.val:
                pre.next = post.next
                post = post.next
            else:
                pre = pre.next
                post = post.next
        return header

s = Solution()
header2 = build([1, 1, 2, 3, 4, 5])
traverse(s.deleteeduplicativeNodes(build([1, 2, 3, 3, 4, 4, 5])))
traverse(s.deleteeduplicativeNodes(build([1, 1, 2, 3, 4, 5])))
traverse(s.deleteeduplicativeNodes(build([1, 2, 3, 4, 5, 5,5])))
