class Solution:
    def getRow(self, rowIndex):
        """
        the solution is similar to two-points.
        :type rowIndex: int
        :rtype: List[int]
        """
        # store previous row
        results = [1]
        if rowIndex <= 0:
            return results
        for i in range(1, rowIndex+1):
            # compute current rows based on previous row
            curLevel=[]
            for j in range(i+1):
                if j == 0 or j == i:
                    curLevel.append(1)
                else:
                    curLevel.append(results[j-1]+results[j])
            results = curLevel
        return results



