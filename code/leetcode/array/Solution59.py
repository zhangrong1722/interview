class Solution59(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        h1, h2=0, n-1
        v1, v2=0, n-1
        value=1
        mat = [[None for _ in range(n)] for _ in range(n)]
        while v1 <= v2 and h1 <= h2:
            # right
            for i in range(h1, h2+1):
                mat[v1][i]=value
                value+=1
            v1 +=1
            # down
            for i in range(v1, v2+1):
                mat[i][h2] = value
                value+=1
            h2 -=1
            # left
            for i in range(h2, h1-1, -1):
                mat[v2][i] = value
                value+=1
            v2 -=1
            # top
            for i in range(v2, v1-1, -1):
                mat[i][h1] = value
                value+=1
            h1 +=1
        return mat
