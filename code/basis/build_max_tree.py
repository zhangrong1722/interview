class MaxTree:
    def buildMaxTree(self, A, n):
        s1, res = list(), list()

        for index in range(n):
            while len(s1) > 0 and A[s1[-1]] < A[index]:
                s1.pop()
            if len(s1) == 0:
                res.append(-1)
            else:
                res.append(s1[-1])
            s1.append(index)

        s1.clear()

        for index in range(n-1, -1, -1):
            while len(s1) > 0 and A[s1[-1]] < A[index]:
                s1.pop()
            if len(s1) > 0 and (res[index] == -1 or A[s1[-1]] < A[res[index]]):
                res[index] = s1[-1]

            s1.append(index)
        return res

s = MaxTree()
s.buildMaxTree([3,1,4,2], 4)
