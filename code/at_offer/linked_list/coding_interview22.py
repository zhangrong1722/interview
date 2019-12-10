"""
题目：链表中倒数第k个节点
     输入一个链表，输出该链表中倒数第k个结点。
思路：
     (1)倒数第k个节点，则是顺数第n-k+1个节点（n为链表长度）；而链表长度，只需要遍历一遍链表；因此该思路需要遍历两遍链表；
     (2)思路(1)需要遍历两次链表，但是思路(2)只需要遍历一遍链表即可；定义两个指针p和q，先将p指针向后移动k个位置，此时p指针和q指针相隔k个位置，接下来
        只需要同时将指针p和q同时向后移动即可，当p指针到末尾时，q指针刚好到达地n-k+1个位置；
     以上两种思路都需要考虑代码的鲁棒性，至少以下三种情况需要单独处理：
     (1)k<=0
     (2)k值大于链表长度
     (3)链表头指针为空
"""
from linked_list import build


class Solution(object):
    def inverseKNode1(self, header, k):
        if header is None or k <= 0:
            return None
        n = 0
        temp = header
        while temp is not None:
            n += 1
            temp = temp.next
        if k > n:
            return None

        temp, index = header, 1
        while temp is not None and index < n - k + 1:
            temp = temp.next
            index += 1
        return temp

    def inverseKNode2(self, header, k):
        if header is None or k <= 0:
            return None
        p, q = header, header
        for i in range(k):
            if p is not None:
                p = p.next
            else:
                return None
        while p is not None and q is not None:
            p, q = p.next, q.next
        return q


s = Solution()
print(s.inverseKNode1(build([1, 3, 5, 2, 4]), 2).val)
print(s.inverseKNode1(build([1, 3, 5, 2, 4]), 3).val)
print(s.inverseKNode1(build([1, 3, 5, 2, 4]), 5).val)
print(s.inverseKNode1(build([1, 3, 5, 2, 4]), 1).val)
print(s.inverseKNode1(build([1, 3, 5, 2, 4]), 10))
print(s.inverseKNode1(None, 2))

print(s.inverseKNode2(build([1, 3, 5, 2, 4]), 3).val)
print(s.inverseKNode2(build([1, 3, 5, 2, 4]), 5).val)
print(s.inverseKNode2(build([1, 3, 5, 2, 4]), 1).val)
print(s.inverseKNode2(build([1, 3, 5, 2, 4]), 2).val)
print(s.inverseKNode2(build([1, 3, 5, 2, 4]), 10))
print(s.inverseKNode2(None, 2))
