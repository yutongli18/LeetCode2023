"""
LCP41.翻转黑白棋
思路有，但是广度优先遍历没有做出来。
"""


from collections import deque


class Solution(object):
    def flipChess(self, chessboard):
        """
        :type chessboard: List[str]
        :rtype: int
        """
        m, n = len(chessboard), len(chessboard[0])

        def judge(chessboard, x, y, dx, dy):
            x += dx
            y += dy
            while 0 <= x < m and 0 <= y < n:
                if chessboard[x][y] == "X":
                    return True
                elif chessboard[x][y] == ".":
                    return False
                x += dx
                y += dy
            return False

        def bfs(chessboard, px, py):
            chessboard = [list(row) for row in chessboard]
            count = 0
            q = deque([(px, py)])
            chessboard[px][py] = "X"

            while q:
                tx, ty = q.popleft()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == dy == 0:
                            continue
                        if judge(chessboard, tx, ty, dx, dy):
                            x, y = tx + dx, ty + dy
                            while chessboard[x][y] != "X":
                                q.append((x, y))
                                chessboard[x][y] = "X"
                                x += dx
                                y += dy
                                count += 1
            return count

        result = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == ".":
                    result = max(result, bfs(chessboard, i, j))
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.flipChess(chessboard=[".X.",".O.","XO."]))
