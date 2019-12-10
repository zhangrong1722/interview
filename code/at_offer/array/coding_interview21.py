"""
题目：调整数组顺序使奇数位于偶数前面
     输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。例如：输入{3,4,5,6,7,8}，输出{3,5,7,4,6,8}
思路一：定义一个指针，从前往后扫描数组，如果遇到偶数，则将后面所有元素往前移动一个位置，此时末尾位置空出来，再将该元素放入末尾位置，该算法时间复杂度为O(n^2)
思路二：定义两个指针pre和post，pre指针从开头位置往末尾扫描，post指针从末尾往前扫描，如果pre位置元素为偶数，则只需要和post位置的奇数互换位置即可，此时算法时间复杂度为O(n)
附：该题目也可将while里的判断条件抽象为一个函数，然后传入函数指针，这样就可以进一步提高可扩展性，解决系列问题，比如将能被3整除的放在不能被3整除的数前面，负数放在整数前面
"""
class Solution1:
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        i = 0
        while i < len(array):
            if array[i] % 2 == 0:
                temp = array[i]
                j = i + 1
                for j in range(i+1, len(array)):
                    array[j-1] = array[j]
                array[j] = temp
            elif self.helper(i+1, array):
                return array
            else:
                i += 1

    def helper(self, index, array):
        for k in range(index, len(array)):
            if array[k] % 2 != 0:
                return False
        return True


class Solution2:
    def reOrderArray(self, array):
        if len(array) <= 1:
            return array
        pre, post = 0, len(array) - 1
        while True:
            while pre < len(array) and array[pre] % 2 != 0:
                pre += 1
            while post >= 0 and array[post] % 2 == 0:
                post -= 1
            if pre <  post:
                array[pre], array[post] = array[post], array[pre]
            else:
                return array


s = Solution1()
print(s.reOrderArray([3, 4, 5, 6, 7, 8]))
print(s.reOrderArray([2, 4, 6, 1, 3, 5, 7]))
print(s.reOrderArray([1, 3, 5, 2, 4, 6]))
print(s.reOrderArray([]))
print(s.reOrderArray([1]))

s2 = Solution2()
print(s2.reOrderArray([3, 4, 5, 6, 7, 8]))
print(s2.reOrderArray([2, 4, 6, 1, 3, 5, 7]))
print(s2.reOrderArray([1, 3, 5, 2, 4, 6]))