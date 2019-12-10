def binary_search(data, k):
    if data is None or len(data) == 0:
        return -1
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if k == data[middle]:
            return middle
        elif k < data[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binary_search([1, 2, 3, 5, 7], 1))
print(binary_search([1, 2, 3, 5, 7], 7))
print(binary_search([1, 2, 3, 5, 7], 3))
print(binary_search([1, 2, 3, 5, 7], 0))