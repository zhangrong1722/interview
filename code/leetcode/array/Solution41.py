class Solution41(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        results=1
        while(results in nums):
            results+=1
        return results