class Solution45(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        reference: https://leetcode.com/problems/jump-game-ii/discuss/18019/10-lines-C%2B%2B-(16ms)-Python-BFS-Solutions-with-Explanations
        BFS solutions: different levels denote the set of reachable nodes in given steps.
        let's say [start, end] denote reachable nodes from current node. each time after a move, udpate start to be end+1 and end to be the farthest node.
        """
        if len(nums) < 2:
            return 0
        n = len(nums)
        start = 0
        end = 0
        max_end = 0
        i = 0
        steps = 0
        # the condition is always True because this problem is solvable.
        while True:
            steps += 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return steps
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end

