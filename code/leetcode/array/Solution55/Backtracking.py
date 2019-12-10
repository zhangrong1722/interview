class Backtracking(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.camJumpFromPosition(0, nums)

    def camJumpFromPosition(self, position, nums):
        """
        backtracking: time limit exceeded
        """
        if (position == len(nums) - 1):
            return True
        right = min(len(nums) - 1, position + nums[position])

        # for furtherPosition in range(position + 1, right + 1):
        #     if self.camJumpFromPosition(furtherPosition, nums):
        #         return True

        # tricks: jump from maximum steps firstly in order to reach the target position quickly as soon as possible
        furtherPosition = right
        while furtherPosition > position:
            if self.camJumpFromPosition(furtherPosition, nums):
                return True
            furtherPosition -=1
        return False
