class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        100340.三角形的最大高度
        :type red: int
        :type blue: int
        :rtype: int
        """
        temp_red, temp_blue = red, blue
        # 第一种情况，第一行从蓝色球开始
        i = 0
        while True:
            if i % 2 == 0:
                if temp_blue - (i + 1) >= 0:
                    temp_blue -= (i + 1)
                    i += 1
                else:
                    break
            else:
                if temp_red - (i + 1) >= 0:
                    temp_red -= (i + 1)
                    i += 1
                else:
                    break
        # print(i)
        temp_red, temp_blue = red, blue
        # 第二种情况，第一行从红色开始
        j = 0
        while True:
            if j % 2 == 0:
                if temp_red - (j + 1) >= 0:
                    temp_red -= (j + 1)
                    j += 1
                else:
                    break
            else:
                if temp_blue - (j + 1) >= 0:
                    temp_blue -= (j + 1)
                    j += 1
                else:
                    break
        return max(i, j)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxHeightOfTriangle(red=4, blue=4))
