class Solution(object):
    def __init__(self):
        self.moves = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

    def judgeCircle(self, moves):
        """
        657.机器人能否返回原点
        :type moves: str
        :rtype: bool
        """
        start = [0, 0]
        for move in moves:
            start[0] += self.moves[move][0]
            start[1] += self.moves[move][1]
        return start[0] == 0 and start[1] == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeCircle(moves="LL"))
