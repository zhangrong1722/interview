class Solution:
    """
    DP based on Exhaustive algorithms to reduce redundancy
    @param height, a list of integer
    @return an integer
    """
    def largestRectangleArea(self, height):
        lens = len(height)
        left = [1] * lens
        right = [1] * lens
        # calculate the left
        # note that when calculating the left sequential traversal needs to be adopted while it is reverse traversal when calculating the right
        # such that previous computations will make sense.As a results,the time complexity is equal to O(n) rather than O(n^2)
        # although two for-loops exists.
        for i in range(lens):
            j = i -1
            while j >=0:
                if height[j] >= height[i]:
                    left[i]+=left[j]
                    j-=left[j]
                else:
                    break
        # calculate the right
        for i in range(lens-1, -1, -1):
            j = i+1
            while j<lens:
                if height[j] >= height[i]:
                    right[i]+=right[j]
                    j+=right[j]
                else:
                    break
        max_rect = 0
        for i in range(lens):
            max_rect = max(max_rect, height[i] * (left[i]+right[i]-1))
        return max_rect
