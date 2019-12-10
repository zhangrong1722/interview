"""
题目：定义栈的数据结构， 请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用min、push及pop的时间复杂度为O(1)
思路：利用辅助栈；辅助栈记录与栈同步 栈顶元素始终放最小元素
"""
class Solution:
    stack, aux_stack = [], []

    def push(self, node):
        self.stack.append(node)
        if len(self.aux_stack) == 0:
            self.aux_stack.append(node)
        else:
            self.aux_stack.append(min(self.aux_stack[-1], node))

    def pop(self):
        if len(self.stack) == 0:
            return None
        self.aux_stack.pop()
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def min(self):
        if len(self.stack) == 0:
            return None
        return self.aux_stack[-1]


s = Solution()
s.push(3)
print(s.stack, s.aux_stack, s.min())

s.push(4)
print(s.stack, s.aux_stack, s.min())

s.push(2)
print(s.stack, s.aux_stack, s.min())

s.push(1)
print(s.stack, s.aux_stack, s.min())

s.pop()
print(s.stack, s.aux_stack, s.min())

s.pop()
print(s.stack, s.aux_stack, s.min())

s.push(0)
print(s.stack, s.aux_stack, s.min())
