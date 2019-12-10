class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2:
            return
        p1 = 0
        p2=p1+1
        curr_lens = len(nums)
        nums.append(nums[curr_lens-1])
        while p1 < curr_lens:
            if nums[p1] == nums[p2]:
                count = p2
                while count < curr_lens and nums[p2] == nums[count]:
                    count+=1
                if count-p2-1 > 0:
                    distance = count - p2 - 1
                    curr_lens -= distance
                    for i in range(p2+1, curr_lens):
                        nums[i] = nums[distance+i]
            p1+=1
            p2+=1
        nums = nums[:curr_lens]
        return curr_lens