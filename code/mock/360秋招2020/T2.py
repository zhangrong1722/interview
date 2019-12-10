"""
在一个古老的国度，这个国家的人并不懂得进位，但是对取模情有独钟，因此诞生了一个经典的问题，
给出两个在m进制下含有n位的数字，你可以分别将这两个数各位上的数字重新排列，然后将两个数按位对应相加并分别对m取模，
这样显然可以得到一个新的m进制下的n位数(可能存在前导0)，但是这个结果是不唯一的，问题来了，按照这样的操作，能够得到的最大的m进制下的数字是多少呢。
"""

import sys
from bisect import bisect_left

def main(m, nums1, nums2):
    pairs = list()
    res = list()

    for i in range(len(nums1)):
        index, cur = -1, -1
        for j in range(len(nums2)):
            if (nums1[i] + nums2[j]) % m > cur:
                index, cur = j, (nums1[i] + nums2[j]) % m

        pairs.append([nums1[i], nums2[index]])
        del nums2[index]

    for n1, n2 in pairs:
        res.append((n1 + n2) % m)

    res.sort(reverse=True)
    for i in range(len(res)):
        if i == len(res) - 1:
            print(res[i])
        else:
            print(res[i], end=' ')




if __name__ == '__main__':
    # line = list(map(int, (sys.stdin.readline().strip().split())))
    # n, m = line[0], line[1]
    # nums1 = list(map(int, sys.stdin.readline().strip().split()))
    # nums2 = list(map(int, sys.stdin.readline().strip().split()))
    nums1,nums2 = [4, 4, 1, 1, 1], [4, 3, 0, 1, 2]
    m = 5
    main(m, nums1, nums2)