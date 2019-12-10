"""
题目：不修改数组找出重复的数字
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的数组。
例如，如果长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的输出是重复的数组2或者3
"""
class Solution(object):
    def auxiliary_array(self, nums):
        """
        因为所有数字都在1~n的范围内，那么可借用一个长度为n+1的辅助数组，下标表示数字，元素值表示该数字出现的次数
        time complexity: O(n)
        space complexity: O(n)
        """
        N = len(nums)
        if N == 0:
            return -1
        for i in range(N):
            if not (nums[i] >= 1 and nums[i] <= N-1):
                return -1

        aux = [0] * N
        for i in range(N):
            if aux[nums[i]] == 0:
                aux[nums[i]] += 1
            else:
                return nums[i]
        return -1

    def const_space(self, nums):
        """
        上述借用辅助数组算法的时间复杂度为O(n)，空间复杂度为O(n)，现在写空间复杂度为O(1)的算法；考虑到所有数字都在1~n范围内，我们可以将1~n分为两部分，
        不难想到，不妨设两部分分别为(1~m)和(m+1~n)，如果数组没有重复元素，必定存在数字1~m出现的次数必然大于m或者数字m+1~n出现的次数必然大于(n-m)次，
        因而我们只需要看数字1~m出现的次数是否是m次，是，则重复数字一定在1~m范围内，否则重复数字在m+1~n范围内。
        按照二分查找法的思想，长度为n的数组，辅助函数helper将会调用O(logn)次，因而最终算法复杂度为 O(nlogn)。空间复杂度为O(1)
        需要注意的是，此算法并不能找出所有的重复数字，比如数组{2, 3, 5, 4, 3, 2, 6, 7}，只能找出3，并不能找到2，原因是在1~2范围内，
        无法确定是每个数字出现1次还是一个元素出现两次。
        相比于辅助数组算法，此算法属于用时间换空间
        time complexity：O(nlogn)
        space complexity：O(1)
        """
        N = len(nums)
        if N == 0:
            return -1
        for i in range(N):
            if not (nums[i] >= 1 and nums[i] <= N - 1):
                return -1
        start, end = 1, N-1
        while start <= end:
            middle = (start + end) // 2
            counts = self.helper(nums, start, middle)
            if counts > middle - start + 1:
                if start == end:
                    return start
                end = middle
            else:
                start = middle + 1

        return -1

    def helper(self, nums, start, end):
        counts = 0
        for e in nums:
            if e >= start and e <= end:
                counts+=1
        return counts

s = Solution()
print(s.const_space([2, 3, 5, 4, 3, 2, 6, 7]))
print(s.const_space([1, 2, 3, 4]))
print(s.const_space([1, 2, 3, 0]))
