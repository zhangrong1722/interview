"""
题目：字符串的排列
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba
    算法：以输入字符串'abc'为例 我们固定第一个字符a 然后将第二个字符与后续字符依次交换
                            同理 我们固定第一个字符b 然后将第二个字符a与后续字符交换位置
                            最后固定第一个字符c 然后将第二字符b与后续字符交换位置
"""
class Solution:
    def Permutation(self, ss):
        results = list()
        if ss is None or len(ss) == 0:
            return results
        self.PermutationHelper(list(ss), 0, results)
        return results

    def PermutationHelper(self, ss, i, results):
        if i == len(ss) - 1 and ''.join(ss) not in results:
            results.append(''.join(ss))
        else:
            for j in range(i, len(ss)):
                ss[i], ss[j] = ss[j], ss[i]
                self.PermutationHelper(ss, i + 1, results)
                ss[i], ss[j] = ss[j], ss[i]

s = Solution()
print(s.Permutation('abbc'))
print(s.Permutation('a'))
print(s.Permutation(None))
print(s.Permutation(''))
