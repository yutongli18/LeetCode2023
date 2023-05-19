"""
1041.困于环中的机器人
考虑一个instructions循环的情况（不要去考虑重复次数的问题）
方向只有四个，“L”和“R”影响最终表现在四个方向上
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirList = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIndex = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == "G":
                x += dirList[dirIndex][0]
                y += dirList[dirIndex][1]
            elif instruction == "L":
                dirIndex -= 1
                dirIndex %= 4
            else:
                dirIndex += 1
                dirIndex %= 4
        return (x == 0 and y == 0) or dirIndex != 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isRobotBounded(instructions="GG"))
