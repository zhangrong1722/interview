class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for num in nums:
            results +=([i + [num] for i in results])
        return results
