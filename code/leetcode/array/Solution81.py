class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums.sort()
        for e in nums:
            if e > target:
                break
            elif e == target:
                return True
        return False