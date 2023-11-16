"""
134.加油站
贪心：当剩余油量的累加和为负数时，说明开始节点必不可能在 [0, index] 区间内。
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        start_index, curr_sum = 0, 0
        for index in range(len(gas)):
            curr_sum += (gas[index] - cost[index])
            if curr_sum < 0:
                start_index = index + 1
                curr_sum = 0
        return start_index


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
