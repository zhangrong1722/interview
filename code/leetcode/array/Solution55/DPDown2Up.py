class DPDown2Up(object):
    def canJump(self, nums):
        """
        Dynamic Programming Down-top
        Top-down to bottom-up conversion is done by eliminating recursion. In practice, this achieves better performance
        as we no longer have the method stack overhead and might even benefit from some caching.:type nums: List[int]
        :rtype: bool
        """
        self.state = dict(UNKNOWN=0, GOOD=1, BAD=-1)
        self.mem = [self.state['UNKNOWN']]*len(nums)
        self.mem[len(nums) - 1] = self.state['GOOD']
        i = len(nums) - 2
        while i >= 0:
            right = min(i + nums[i], len(nums)-1)
            for j in range(i + 1, right+1):
                if self.mem[j] == self.state['GOOD']:
                    self.mem[i] = self.state['GOOD']
                    break
            # self.mem[i] = self.state['BAD']
            i -= 1
        return self.mem[0] == self.state['GOOD']
