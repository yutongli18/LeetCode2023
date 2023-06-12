"""
36.有效的数独
"""


def checkVerify(strList):
    checkList = []
    for char in strList:
        if char != ".":
            if char in checkList:
                return False
            checkList.append(char)
    return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):  # 行
            if not checkVerify(board[i]):
                return False
        for j in range(9):
            checkList = []
            for i in range(9):
                checkList.append(board[i][j])
            if not checkVerify(checkList):
                return False
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                checkList = [board[i-1][j-1], board[i-1][j], board[i-1][j+1],
                             board[i][j-1], board[i][j], board[i][j+1],
                             board[i+1][j-1], board[i+1][j], board[i+1][j+1]]
                if not checkVerify(checkList):
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku(board=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

