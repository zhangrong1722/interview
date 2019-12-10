# Brute Force(backtracking): 246 / 313 test cases passed.
# class Solution:
#     def threeSum(self, nums):
#         res, temp = list(), list()
#         nums.sort()
#         self.helper(nums, 0, 0, res, temp)
#         return res
#
#     def helper(self, nums, index, s, res, temp):
#         if index >= len(nums) or len(temp) == 3:
#             if s == 0 and len(temp) == 3:
#                 if temp.copy() not in res:
#                     res.append(temp.copy())
#         else:
#             temp.append(nums[index])
#             s += nums[index]
#             self.helper(nums, index + 1, s, res, temp)
#
#             temp.pop()
#             s -= nums[index]
#             self.helper(nums, index + 1, s, res, temp)


# two-pointer: 311 / 313 test cases passed.
# class Solution:
#     def threeSum(self, nums):
#         res, temp, n = list(), list(), len(nums)
#         if n < 3:
#             return res
#         nums.sort()
#         for index in range(n):
#             left, right = index + 1, n - 1
#             while left < right:
#                 s = nums[index] + nums[left] + nums[right]
#                 if s == 0:
#                     if [nums[index], nums[left], nums[right]] not in res:
#                         res.append([nums[index], nums[left], nums[right]])
#                     left += 1
#                 elif s < 0:
#                     left += 1
#                 else:
#                     right -= 1
#
#         return res

# optimal
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            maps = dict()
            j = i + 1
            while j < len(nums):
                req = -nums[i] - nums[j]
                if req in maps:
                    res.append([nums[i], req, nums[j]])
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j += 1
                else:
                    maps[nums[j]] = j

                j += 1

        return res
