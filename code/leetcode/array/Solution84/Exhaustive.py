class Solution:
    def largestRectangleArea(self, heights):
        """
        exhaustive algorithm: time limit exceeded
        time complexity: O(n^2)
        :type heights: List[int]
        :rtype: int
        """
        results = 0
        for i in range(len(heights)):
            width = 0
            for left in range(i, -1, -1):
                if heights[i] <= heights[left]:
                    width+=1
                else:
                    break
            for right in range(i+1, len(heights)):
                if heights[i] <= heights[right]:
                    width+=1
                else:
                    break
            results = max(results, heights[i] * width)
        return results
