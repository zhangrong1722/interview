class Solution:
    def maxProduct(self, nums):
        """
        use two array to store max and min value
        :type nums: List[int]
        :rtype: int
        two arrays to store max and min.
        reference: https://leetcode.com/problems/maximum-product-subarray/discuss/174563/DP-C%2B%2B-simple
        """
        min_arr, max_arr = [0] * len(nums), [0] * len(nums)
        min_arr[0]=nums[0]
        max_arr[0]=nums[0]
        for i in range(1, len(nums)):
            min_arr[i] = min(min(min_arr[i-1]*nums[i], max_arr[i-1]*nums[i]), nums[i])
            max_arr[i] = max(max(min_arr[i-1]*nums[i], max_arr[i-1]*nums[i]), nums[i])

        return max(max(min_arr), max(max_arr))