"""
题目：最长不含重复字符的子字符串
     请从字符串中找出一个最长的不包含重复字符的子字符串 计算该最长子字符串的长度 假设字符串中只包含'a'-'z'的字符 例如 在字符串'arabcacfr'中
     最长的不含重复字符的子字符串是'acfr' 长度为4
思路：最暴力的方法是直接找出所有子字符串 然后逐个判断是否含有重复字符串 该方法最大的问题就是效率问题 找出所有连续子串的时间复杂度是O(n^2) 判断是否
     包含重复字符的时间复杂度是O(n) 因此该暴力算法的时间复杂度是O(n^3) 不可取
     接下来以字符串'arabcacfr'为例用动态规划方法来分析：用dp[i]表示以i位置结尾的最长子字符串长度 对于第i位置的字符 分以下两种情况分析：
     (1)如果i位置字符未出现 则dp[i]=dp[i-1]+1 例如i=1时 dp[1]=dp[0]+1
     (2)如果i位置字符出现过 此处情况稍微有点复杂 设该字符上次出现到此次出现之间的子串长度为d 可分以下两种情况分析：
        (a)当d<=dp[i-1] 说明长度为d的子串比的长度不超过i-1位置元素结尾的最长子串 对于dp[i-1] 说明pos-(i-1)之间木有重复元素 因此
           (pos+1)~(i-1)也是也没有重复元素 再加上在pos~(i-1)之间i位置元素未出现过 因此dp[i]=i-pos
           此时dp[i]=i- pos 例如i=2,5
        (b)当d>dp[i-1] 也就是i=8时 此时d=7=>dp[7]=3 由于r在后续字符串中没出现过 所以dp[8]=dp[7]+1=4
"""


class Solution(object):
    def LongestNoepetitionSubstring(self, ss):
        if ss is None or len(ss) == 0:
            return 0
        dp, pos = [1] * len(ss), [-1] * len(ss)
        # 计算每个字符上次出现的位置
        for i in range(len(ss) - 1, -1, -1):
            pos[i] = ss[:i].rfind(ss[i]) if ss[:i].rfind(ss[i]) != -1 else -1

        for i in range(1, len(ss)):
            if pos[i] == -1:
                dp[i] = dp[i - 1] + 1
            elif i - pos[i] > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - pos[i]
        print(dp)
        return max(dp)


s = Solution()
print(s.LongestNoepetitionSubstring('arabcacfr'))
