class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums, multiple = 0, 1

        for e in digits[::-1]:
            nums += multiple * e
            multiple*=10
        nums+=1
        results = []
        while nums > 0:
            results.append(nums%10)
            nums //=10
        return results[::-1]

s = Solution()
print(s.plusOne([9,1,2]))