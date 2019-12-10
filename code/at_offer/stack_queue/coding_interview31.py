"""
题目：栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路：序列{1,2,3,4,5}和{4,5,3,2,1}，出栈序列第一个元素是4，因此需要将1，2，3压入栈，下一个出栈元素是5，栈顶元素是3，因此需要将5压入栈，再出栈，接下来是3、2、1，依次出栈
"""
class Solution(object):
    def isPopOrder(self, pushV, popV):
        if pushV is None or popV is None or len(pushV) == 0 or len(popV) == 0:
            return False

        aux_stack = []
        i, j = 0, 0
        for i in range(len(pushV)):
            aux_stack.append(pushV[i])
            if pushV[i] == popV[0]:
                break

        while True:
            # j达到list末尾 辅助栈为空时 则表明匹配成功
            if j == len(popV) and len(aux_stack) == 0:
                return True
            # 当辅助栈顶元素不等于当前匹配元素 入栈序列没有元素时 则表明匹配失败
            if aux_stack[-1] != popV[j] and len(pushV) == i:
                return False
            # 在栈顶元素 则直接弹出
            if aux_stack[-1] == popV[j]:
                aux_stack.pop()
                j += 1
            # 不在栈顶元素 则压入新元素
            else:
                i += 1
                while i < len(pushV):
                    aux_stack.append(pushV[i])
                    if pushV[i] == popV[j]:
                        break
                    i += 1


s = Solution()
print(s.isPopOrder([1, 2, 3, 4 ,5], [4, 5, 3, 2, 1]))
print(s.isPopOrder([1, 2, 3, 4 ,5], [4, 3, 5, 1, 2]))
print(s.isPopOrder([1], [1]))
print(s.isPopOrder(None, None))