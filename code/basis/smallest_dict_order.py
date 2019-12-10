class Prior:
    def findSmallest(self, strs, n):
        temp = [''] * n
        self.merge_sort(strs, 0, n - 1, temp)
        print(strs)
        return ''.join(strs)
    
    def merge_sort(self, strs, left, right, temp):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort(strs, left, middle, temp)
            self.merge_sort(strs, middle + 1, right, temp)
            self.merge(strs, left, middle, right, temp)
    
    def merge(self, strs, left, middle, right, temp):
        start, end, pos =  middle, right, right
        while start >= left and end >= middle + 1:
            if strs[start] + strs[end] > strs[end] + strs[start]:
                temp[pos] = strs[start]
                pos -= 1
                start -= 1
            else:
                temp[pos] = strs[end]
                pos -= 1
                end -= 1
        while start >= left:
            temp[pos] = strs[start]
            pos, start = pos - 1, start - 1

        while end >= middle + 1:
            temp[pos] = strs[end]
            pos, end = pos - 1, end - 1
        print(temp)

        strs[left: right + 1] = temp[left: right + 1]

s = Prior()
s.findSmallest(["kid","yqt","i","k"], 4)