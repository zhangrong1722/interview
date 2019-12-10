import random

class SortAlgorithm(object):
    def bubble_sort(self, arr):
        if arr is None or len(arr) == 0:
            return
        n = len(arr)
        for i in range(n-1):
            # early stopping if sorted
            flag = True
            for j in range(0, n-i-1):
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    flag = False
            if flag:
                return
    # simple version
    def bubble_sort1(self, arr):
        if arr is None or len(arr) == 0:
            return
        n = len(arr)
        for i in range(n):
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def insertion_sort(self, arr):
        if arr is None or len(arr) == 0:
            return
        n = len(arr)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

    def selection_sort(self, arr):
        if arr is None or len(arr) == 0:
            return
        n = len(arr)
        for i in range(n):
            flag = True
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    flag = False
            if flag:
                return

    def merge_sort(self, arr, left, right, temp):
        if left < right:
            # divide
            middle = (left + right) // 2
            self.merge_sort(arr, left, middle, temp)
            self.merge_sort(arr, middle+1, right, temp) 
            # merge
            self.merge_sort_helper(arr, left, middle, right, temp)

    def merge_sort_helper(self, arr, left, middle, right, temp):
        """
        """
        i, j, pos = middle, right, right
        while i >= left and j >= middle + 1:
            if arr[i] > arr[j]:
                temp[pos] = arr[i]
                i -= 1
            else:
                temp[pos] = arr[j]
                j -= 1
            pos -= 1

        while i >= left:
            temp[pos] = arr[i]
            i -= 1
            pos -= 1

        while j >= middle + 1:
            temp[pos] = arr[j]
            j -= 1
            pos -= 1
        arr[left: right + 1] = temp[left: right + 1]
        # for k in range(left, right + 1):
            # arr[k] = temp[k]

    def merge_sort_testor(self, arr):
        temp = [-1] * len(arr)
        self.merge_sort(arr, 0, len(arr) - 1, temp)

    def quick_sort(self, arr, left, right):
        if left < right:
            index = self.partition(arr, left, right)
            self.quick_sort(arr, left, index - 1)
            self.quick_sort(arr, index + 1, right)

    def partition(self, arr, left, right):
        element = arr[left]
        while left < right:
            while left < right and arr[right] >= element:
                right -= 1

            if arr[right] < element:
                arr[left], arr[right] = arr[right], arr[left]

            while left < right and arr[left] <= element:
                left += 1

            if arr[left] > element:
                arr[left], arr[right] = arr[right], arr[left]
        return left

    def heap_sort(self, arr):
        for index in range(len(arr)//2 - 1, -1, -1):
            self.adjust_heap(arr, index, len(arr) - 1)

        for index in range(len(arr)-1, 0, -1):
            arr[0], arr[index] = arr[index], arr[0]
            self.adjust_heap(arr, 0, index - 1)

    def adjust_heap(self, arr, root_pos, length):
        node = 2 * root_pos + 1
        while node <= length:
            if node + 1 <= length and arr[node + 1] > arr[node]:
                node = node + 1

            if arr[root_pos] < arr[node]:
                arr[root_pos], arr[node] = arr[node], arr[root_pos]
                root_pos = node
                node = 2 * root_pos + 1
            else:
                break
    
    def shell_sort(self, arr):
        increment = len(arr)
        while increment > 1:
            increment = increment // 3 + 1
            # the above is extremely similar to insertion-sort algorithm
            for i in range(increment, len(arr)):
                for j in range(i, 0, -increment):
                    if arr[j] < arr[j - increment]:
                        arr[j], arr[j - increment] = arr[j - increment], arr[j]

s = SortAlgorithm()
arr = random.sample(range(1, 10000), 200)

# s.bubble_sort(arr)
# s.selection_sort(arr)
# s.bubble_sort1(arr)
s.insertion_sort(arr)
# s.merge_sort_testor(arr)
# s.quick_sort(arr, 0, len(arr) - 1)
# s.heap_sort(arr)

# s.shell_sort(arr)

print(arr)