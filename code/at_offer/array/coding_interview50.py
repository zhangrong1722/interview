"""
题目：第一个只出现一次的字符
思路：最直观的方法是第一次遍历字符串 遍历到每一个位置时 在后续查找该元素是否出现 此时算法复杂度为O()
     第二种方式是使用空间换时间 新建一个字典 遍历是存储每个元素出现的频率 再遍历该字典（哈希表）即可
相关题目：（1）定义一个函数，输入两个字符串，从第一个字符串中删除第二个字符串中出现的所有字符
        （2）定义一个函数，删除字符串中有所重复出现的字符
        （3）判断两个单词是否为变位词（即两个单词中出现的字符相同 且出现次数也相同）
"""
class Solution(object):
    def FirstCharWith1Times(self, arr):
        if arr is None or len(arr) == 0:
            return None
        freq = dict()
        for e in arr:
            if e not in freq.keys():
                freq[e] = 1
            else:
                freq[e] += 1
        for k, v in freq.items():
            if v == 1:
                return k

s = Solution()
print(s.FirstCharWith1Times('abaccdeff'))