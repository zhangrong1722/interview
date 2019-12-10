"""
题目：复杂链表的复制
     输入一个复杂链表（每个节点中有节点值 以及两个指针 一个指向下一个节点 另一个特殊指针指向任意一个节点）返回结果为复制后复杂链表的head
思路：以A->B->C->D->E为例
     方法一：复制原始链表中的每一个节点 再用next指针连接起来 此时链表状态如下 A->A'->B->B'->C->C'->D->D'->E->E' 然后需要修改random指针 以A'为例 为了
            寻找random指向 因此需要从头开始遍历遍历 因此最终时间复杂度为O(n^2)
     方法二：方法一的时间复杂度的消耗主要在寻找random指针 为了降低时间复杂度 我们采用以空间换时间 在复制链表时 我们用一个字典存储random指针位置
            因此在修改random指针时 我们可在O(1)时间内定位 最终我们可将时间复杂度从O(n^2)降低到O(n)
     方法三：我们在方法二的基础上 不使用辅助空间来实现线性复杂度 假设S节点复制节点为S' S的random指针指向N节点 N节点的复制节点为N' 因为S的next指向S'
            N的next指向N' 因此可直接通过S的random指针定位S'的random指针
     最后一步均是分割两个链表
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def clone(self, pHead):
        if pHead is None:
            return None
        self.__cloneNodes(pHead)
        self.__connectRandomNodes(pHead)
        return self.__reconnectNodes(pHead)

    def __cloneNodes(self, pHead):
        p = pHead
        while p is not None:
            q = RandomListNode(p.label)
            q.next = p.next
            p.next = q
            p = p.next.next

    def __connectRandomNodes(self, pHead):
        p = pHead
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next

    def __reconnectNodes(self, pHead):
        pCloneHead, pCloneNode, p = None, None, pHead

        pCloneHead = pCloneNode = p.next
        p.next = pCloneNode.next
        p = p.next

        while p is not None:
            pCloneNode.next = p.next
            pCloneNode = pCloneNode.next
            p = pCloneNode.next
        return pCloneHead


# 测试用例一
# pHead = RandomListNode(1)
# node1 = RandomListNode(2)
# node2 = RandomListNode(3)
# node3 = RandomListNode(4)
# node4 = RandomListNode(5)
# pHead.next = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4
# pHead.random = node2
# node1.random = node4
# node3.random = node1
#
# s = Solution()
# s.clone(pHead)

# 测试用例二 出现环
# pHead = RandomListNode(1)
# node1 = RandomListNode(2)
# node2 = RandomListNode(3)
# pHead.next = node1
# node1.next = node2
# pHead.random = node2
# node2.random = pHead
#
# s = Solution()
# pHead = s.clone(pHead)
# print(pHead)

# 测试用例三：一个节点random指针指向自身
# pHead = RandomListNode(1)
# node1 = RandomListNode(2)
# node2 = RandomListNode(3)
# pHead.next = node1
# node1.next = node2
# pHead.random = pHead
#
# s = Solution()
# pHead = s.clone(pHead)
# print(pHead)
