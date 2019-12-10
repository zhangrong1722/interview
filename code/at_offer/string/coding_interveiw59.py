"""
题目：滑动窗口的最大值
     给定一个数组和滑动窗口的大小 请找出所有滑动窗口里的最大值 例如 输入数组{2,3,4,2,,6,2,5,1}及滑动窗口的大小3 那么一共存在6个滑动窗口 它们
     的最大值分别为{4,4,6,6,6,5}
思路一：比较暴力的直接蛮力法 假设滑动窗口大小为k 在一个滑动窗口中找出最大值的复杂度是O(k) 数组长度为n 则整体时间复杂度为O(nk)
思路二：思路一显然是不可取的 时间复杂度比较高 我们可以借用一个长度大小为k的队列 保存滑动窗口 剩下的工作就是返回当前状态下长度大小为k的队列最大值了
"""
from queue import Queue


class Solution(object):
    def MaxValueInSlidingWindow(self, data, k):
        if data is None or k <= 0 or len(data) < k:
            return []

        q, lens, results = Queue(), len(data), list()
        # 初始化状态
        q.put(data[0])
        curMax, index = data[0], 1

        while index < lens:
            if q.qsize() < k:
                curMax = max(curMax, data[index])
                q.put(data[index])
            else:
                q.put(data[index])
                q.get()
                curMax = max(curMax, data[index])
                results.append(curMax)
            index += 1
        return results

s = Solution()
print(s.MaxValueInSlidingWindow([2, 3, 4,2, 6,2,5,1], 3))



