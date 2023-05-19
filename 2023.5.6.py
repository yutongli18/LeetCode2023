"""
1419.数青蛙
模拟问题。
关键在于记录同时发出蛙鸣的青蛙数。
为了避免超出时间限制，不记录完整的字符串，只记录前一个字符。
"""


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        croakLength = len(croakOfFrogs)
        if croakLength % 5 > 0:
            return -1

        modeMap = {"c": 0, "r": 1, "o": 2, "a": 3, "k": 4}
        count = [0] * 4
        frogsNum, minFrogsNum = 0, 0
        for char in croakOfFrogs:
            mode = modeMap[char]
            if mode == 0:
                frogsNum += 1  # 一只青蛙开始鸣叫
                count[mode] += 1
            else:
                if count[mode-1] < 1:
                    return -1
                count[mode-1] -= 1
                if mode == 4:
                    frogsNum -= 1  # 一只青蛙结束鸣叫（在下一轮时它可以再次发出鸣叫）
                else:
                    count[mode] += 1
            minFrogsNum = max(minFrogsNum, frogsNum)  # 在整个蛙鸣过程中，最大的蛙鸣数就是答案
        if frogsNum > 0:
            return -1
        return minFrogsNum


if __name__ == '__main__':
    sol = Solution()
    print(sol.minNumberOfFrogs(croakOfFrogs="croakcroak"))
