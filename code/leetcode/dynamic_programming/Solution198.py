class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0]*len(nums)
        dp[0] = 1
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[1], nums[0]+nums[2])
        for i in range(3, len(nums)):
            dp[i] = max(nums[i], dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]

s = Solution()
print(s.rob([2,7,9,3,1]))