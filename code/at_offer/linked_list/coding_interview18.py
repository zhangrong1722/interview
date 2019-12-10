"""
题目：在O(1)时间内删除链表节点
     给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
思路：在单向链表中删除一个节点，常规思路无疑是从链表的头节点开始，顺序遍历来查找要删除的节点，并在链表中删除该节点，需要注意的是这种方式下给定的往往是节点值，而非节点指针，此时时间复杂度为 O(n)
     而题目要求再O(1)时间内，因此需要另谋他法；例如，一个单链表如下：1->2->3->4->5，如果要删除节点3，除了从头查找外，我们也可以充分利用给定要删除节点的指针这一信息，
     即可以用待删除节点的下一节点来覆盖待删除节点，然后删除下一节点。如果是前(n-1)个节点，对应时间复杂度为O(1)，最后一个节点由于没有后续节点，因此需要从头开始查找待删除节点，此时时间复杂度为O(n)，
     但是最终的时间复杂度=(n-1+n)/2，仍然是O(1)时间复杂度
"""
from linked_list import traverse, build


class Solution(object):
    def deleteNode(self, header, toBeDeletedNode):
        if header == None or toBeDeletedNode == None:
            return header
        # 尾节点
        if toBeDeletedNode.next is None:
            temp = header
            while temp is not None and temp.next != toBeDeletedNode:
                temp = temp.next
            temp.next = toBeDeletedNode.next
        else:
            temp = toBeDeletedNode.next
            toBeDeletedNode.val = temp.val
            toBeDeletedNode.next = temp.next
        return header

s = Solution()
header = build([1, 2, 3, 4, 5])
traverse(s.deleteNode(header, None))
traverse(s.deleteNode(header, header.next.next))
traverse(s.deleteNode(header, header.next.next.next.next))
traverse(s.deleteNode(header, header))