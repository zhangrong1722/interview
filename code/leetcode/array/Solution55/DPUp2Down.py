class DPTop2Down(object):
    def canJump(self, nums):
        """
        Dynamic Programming Top-down
        Top-down dynamic programming could be seen as optimized backtracking, which relies on the observation that
        the results will be never changed once a position is reachable to target so we just need to store this results.
        Initially,all position except target position are unknown.
        :type nums: List[int]
        :rtype: bool
        """
        self.state = dict(UNKNOWN=0, GOOD=1, BAD=-1)
        self.mem = [self.state['UNKNOWN']]*len(nums)
        self.mem[len(nums) - 1] = self.state['GOOD']
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position, nums):
        if position == len(nums)-1:
            return True
        if (self.mem[position] != self.state['UNKNOWN']):
            return True if self.mem[position] == 'GOOD' else False
        right = min(position + nums[position], len(nums) - 1)

        for furtherPosition in range(position + 1, right+1):
            if (self.canJumpFromPosition(furtherPosition, nums)):
                self.mem[furtherPosition] = 'GOOD'
                return True

        self.mem[position] = 'BAD'
        return False
