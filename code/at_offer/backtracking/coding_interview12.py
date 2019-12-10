"""
题目：矩阵中的路径
     请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
     路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
     如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
     例如 a b c e
         s f c s
         a d e e
     这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
思路分析：这是一个运用回溯法的典型题目。下面以上述例子为例进行分析：由于目标字符串第一个字符为b，因此我们用(0,1)位置开始寻找，回溯法的主要思想是依次遍历每个节点的可选选项，
        如此往复；如果不满足条件，则返回上一级节点，下面可以用树形结构来表示上述查找过程：
                            b
                        |   |   |
                        a   f   c
                              |   |
                              c   e
                            |   |
                            e   s
                          |   |
                          d   e
        从(0,1)位置开始，可往左、下和右三个方向寻找，考虑到目标字符串第二个字符是c，我们只能往右走即位置c，同理，可往右边、下边走，但是考虑到第三个元素是c，故只能往下走，如此直到找到目标路径
        还需要注意的是：题目中要求不能重复走相同位置，所以还需一个数组来表示一个位置是否已经被探测

"""
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """
        :param matrix: 目标矩阵
        :param rows: 矩阵行数
        :param cols: 矩阵列数
        :param path: 目标路径
        :return: 如果能找到，则返回True；否则，返回False
        """
        if rows == 0 or cols == 0:
            return False
        for i in range(rows):
            for j in range(cols):
                visited = [False] * (rows * cols)
                if self.helper(matrix, i, j, rows, cols, path, 0, visited):
                    return True
        return False

    def helper(self, matrix, row, col, rows, cols, path, pathLength, visited):
        if pathLength == len(path):
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row * cols + col] != path[pathLength] or visited[row * cols + col]:
            return False
        visited[row * cols + col] = True
        return self.helper(matrix, row, col - 1, rows, cols, path, pathLength + 1, visited) or self.helper(matrix, row, col + 1, rows, cols, path, pathLength + 1, visited) or self.helper(matrix, row - 1,  col, rows, cols, path, pathLength + 1, visited) or self.helper(matrix, row + 1, col, rows, cols, path, pathLength + 1, visited)


s = Solution()
# print(s.hasPath('ABCESFCSADEE', 3, 4, 'ABCB'))
# ABCCED
# print(s.hasPath('ABCESFCSADEE', 3, 4, 'ABCCED'))
print(s.hasPath('ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5,8,"SGGFIECVAASABCEHJIGQEM"))