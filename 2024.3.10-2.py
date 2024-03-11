"""
100247.幸福值最大化的选择方案
"""


class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            total += max(happiness[i] - i, 0)
        return total


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumHappinessSum(happiness=[12, 1, 42], k=3))
