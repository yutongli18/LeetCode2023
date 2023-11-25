class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start_point = -1
        if sum(gas) < sum(cost):
            return start_point
        start_point = 0
        rest = 0
        for i in range(len(gas)):
            rest += gas[i]
            rest -= cost[i]
            if rest < 0:
                rest = 0
                start_point = i + 1
        return start_point


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
