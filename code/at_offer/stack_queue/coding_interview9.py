"""
题目：用两个栈实现一个队列
用两个栈实现一个队列 假设两个栈分别为s1，s2；过程如下：
(1)入队：直接压入栈s1
(2)出队：如果s2为空，则将s1所有元素出栈压入s2，再s2出栈；否则，直接s2出栈
"""
class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
