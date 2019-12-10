from collections import deque

class SlideWindow:
    def slide(self, arr, n, w):
        if n <= 1:
            return []
        res, d = list(), deque()

        for index in range(n):
            while len(d) > 0 and arr[index] >= arr[d[-1]]:
                d.pop()
            d.append(index)
            if index >= w - 1:
                while index - d[0] >= w:
                    d.popleft()
                max_value_index = d[0]
                res.append(arr[max_value_index])
        return res

s = SlideWindow()
# print(s.slide([357,564,212,500,96],5,3))
# print(s.slide([36,445,234],3,1))
print(s.slide([4,3,5,4,3,3,6,7],8,3))