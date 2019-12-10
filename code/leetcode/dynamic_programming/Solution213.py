class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Compared with House Robber I,the differences are following: (1)All house are arranged in a circle,which force us to have to consider the first house is robbed.
        Hence,we need to consider these two case respectively.We also can solve this two sub-problems by a 1D array dp such that i-th element in dp stores max profile up to i-th house.
        reference: https://leetcode.com/problems/house-robber-ii/discuss/213378/Python-DP-O(n)-Solution-with-explanation-using-2-DP-arrays
        """
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums)
        select_first, skip_first = [0] * N, [0] * N
        select_first[0], select_first[1] = nums[0], nums[0]
        skip_first[1] = nums[1]
        for i in range(2, N):
            select_first[i] = max(nums[i]+select_first[i-2], select_first[i-1]) if i != N-1 else select_first[i-1]
            skip_first[i] = max(nums[i]+skip_first[i-2], skip_first[i-1])
        return max(select_first[N-1], skip_first[N-1])
