"""
题目：找出数组中的重复数字
在一个长度为n的数组里的所有数字都在0~n-1范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3},那么对应的输出是重复的数字2或者3
"""
class Solution(object):
    def sort(self, nums):
        """
        将数组重新排列，再依次遍历数组，如果nums[i]!=i，则输出。-1表示没有重复数字。
        time complexity: O(nlogn)
        space coomplexity: O(1)
        """
        N = len(nums)
        if N == 0:
            return -1
        for i in range(N):
            if not (nums[i] >= 0 and nums[i] <= N-1):
                return -1
        sorted(nums)
        for i in range(N):
            if i != nums[i]:
                return nums[i]

        return -1

    def hash_map(self, nums):
        """
        借用字典结构；key元素，遍历数组，如果元素不在字典里，则跳过，否则，该元素重复
        time complexity: O(n)
        space complexity: O(n)
        """
        N = len(nums)
        if N == 0:
            return -1
        for i in range(N):
            if not (nums[i] >= 0 and nums[i] <= N-1):
                return -1

        freq = dict()
        for e in nums:
            if e in freq.keys():
                return e
            else:
                freq[e]=1
        return -1

    def resort(self, nums):
        """
        考虑到数组中有所数字都在0~n-1范围内，如果数组没重复，则重新排序后，对任意位置i有i=nums[i];否则，必然存在有些位置有多个元素，
        或者空位置。因此，我们可以依次遍历元素，如果i!=nums[i]（记为m）,此时我们需要将m换到对应位置m去，
        即我们只需要交换m和nums[m]。如果出现m=nums[m]，则说明m是重复元素
        """
        N = len(nums)
        if N == 0:
            return -1
        for i in range(N):
            if not (nums[i] >= 0 and nums[i] <= N-1):
                return -1
        for index in range(N):
            while index != nums[index]:
                if nums[index] == nums[nums[index]]:
                    return nums[index]
                # 将元素nums[index]和nums[nums[index]]互换
                temp = nums[index]
                nums[index] = nums[nums[index]]
                nums[temp] = temp
        return -1


s = Solution()
print(s.resort([2,3,1,0,0,5,4]))