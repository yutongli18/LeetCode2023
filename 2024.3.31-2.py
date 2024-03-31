"""
100235.换水问题 II
"""


class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        # b：剩余的水量，e：交换用的空瓶
        b, e = numBottles, numExchange
        total = 0
        while b >= e:
            total += e
            b = b - e + 1
            e += 1
        return total + b


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxBottlesDrunk(numBottles=10, numExchange=3))
