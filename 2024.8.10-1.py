class Solution:
    def __init__(self):
        self.pos = [0, 0]
        self.direction = 0
        self.steps = [[0, 1], [-1, 0], [0, -1], [1, 0]]

    def getPosition(self, S):
        """
        1.走路的最后位置
        :param S:
        :return:
        """
        for i in range(len(S)):
            op = S[i]
            if op == "W":
                self.pos[0] += self.steps[self.direction][0]
                self.pos[1] += self.steps[self.direction][1]
            elif op == "A":
                self.direction = (self.direction + 1) % len(self.steps)
            elif op == "D":
                self.direction = (self.direction - 1 + len(self.steps)) % len(self.steps)
        return self.pos


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPosition("WWW"))
