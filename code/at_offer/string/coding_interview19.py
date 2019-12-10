"""
题目：正则表达式匹配
     请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
     在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
思路：题目难点在于有'*'时的匹配策略，如果没有'*'只有'.'时，比较容易匹配；如果遇到'.'，则该位置任意字符直接匹配；但是遇到'*'时就比较复杂。主要情况如下:
     下一个字符是'*'：
     如果当前字符匹配（包含字符串和模式串对应位置相同和模式串为'.'两种情况）：
     (1)模式串向后移动两个位置，字符串不动，相当于忽略串x*，当前字符匹配0次
     (2)模式串不动，字符串向后移动一个位置，相当于匹配多个x
     (3)模式串移动两个位置，字符串移动一个位置，相当于当前字符匹配一次
     下一字符不是'*'：
     如果当前字符匹配，则模式串和字符串各自移动一个位置继续匹配
     结束条件：如果都字符串和模式串都匹配到最后一个位置，则匹配成功；当模式串到最后一个位置，但是字符串没有到最后一个位置，则匹配失败；需要注意：反过来则不能判断匹配成功与否
     另外coding时需要小心数组边界条件的判定，这里极易容易出错
"""
class Solution:
    def match(self, s, pattern):
        if s is None or pattern is None:
            return False
        # if
        return self.helper(s, pattern, 0, 0)

    def helper(self, s, pattern, strIndex, paIndex):
        if strIndex == len(s) and paIndex == len(pattern):
            return True
        if strIndex != len(s) and paIndex == len(pattern):
            return False
        if paIndex + 1 < len(pattern) and pattern[paIndex + 1] == '*':
            if (strIndex < len(s) and pattern[paIndex] == s[strIndex]) or (pattern[paIndex] == '.' and strIndex < len(s)):
                return self.helper(s, pattern, strIndex, paIndex + 2) or self.helper(s, pattern, strIndex + 1, paIndex) or self.helper(s, pattern, strIndex + 1, paIndex + 2)
            else:
                return self.helper(s, pattern, strIndex, paIndex + 2)
        if paIndex < len(pattern) and strIndex < len(s) and (pattern[paIndex] == s[strIndex] or pattern[paIndex] == '.'):
            return self.helper(s, pattern, strIndex + 1, paIndex + 1)
        return False


s = Solution()
# print(s.match("",""))
# print(s.match("", ".*"))
print(s.match("a",".*"))
print(s.match("a", "."))

