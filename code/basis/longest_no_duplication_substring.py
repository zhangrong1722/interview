class DistinctSubstring:
    def longestSubstring(self, A, n):
        if n<=1:
            return n
        res, last_pos_dict, pre = [1] * n, dict(), 0
        last_pos_dict[A[0]] = 0

        for i in range(1, n):
            if A[i] in last_pos_dict:
                last_pos = last_pos_dict[A[i]]
                if pre <= last_pos:
                    res[i] = i - last_pos
                    pre = last_pos + 1
                else:
                    res[i] = res[i-1] + 1
            else:
                res[i] = res[i-1] + 1
                pre = i - res[i]

            last_pos_dict[A[i]] = i
        return max(res)

s = DistinctSubstring()
s.longestSubstring('rfrxkmdb', 8)