class Solution:
    def exist(self, board, word):
        """
        recursive searching from first matching char.
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.rows, self.cols = len(board), len(board[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.lens = len(word)
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] == word[0] and self.find(board, i, j, 0, word):
                    return True
        return False

    def find(self, board, i, j , index, word):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or word[index] != board[i][j] or self.visited[i][j]:
            return False

        if index == len(word)-1:
            return True

        self.visited[i][j] = True
        if self.find(board, i+1, j, index+1, word) or self.find(board, i-1, j, index+1, word) or self.find(board, i, j-1, index+1, word) or self.find(board, i, j+1, index+1, word):
            return True
        self.visited[i][j] = False
        return False
