class Greedy(object):
    def canJump(self, nums):
        """
        greedy algorithm: jump the leftmost step each time and the local optimal solution is equal to the global optimal solution in this issue.
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            if lastPos <= i + nums[i]:
                lastPos = i
            i -= 1
        return lastPos == 0