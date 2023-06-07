"""
2611.老鼠和奶酪
贪心+排序
"""


class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(reward1)
        rewards = zip(reward1, reward2)
        rewards = sorted(rewards, key=lambda x: x[1] - x[0], reverse=True)
        # print(rewards)
        # total = sum([reward[0] for reward in rewards[:k]]) + sum([reward[1] for reward in rewards[k:]])
        total = sum(reward1)
        for i in range(n - k):
            total = total - rewards[i][0] + rewards[i][1]
            # print(total)
        return total


if __name__ == '__main__':
    sol = Solution()
    # sol.miceAndCheese(reward1=[4, 1, 5, 3, 3], reward2=[3, 4, 4, 5, 2], k=3)
    print(sol.miceAndCheese(reward1=[4, 1, 5, 3, 3], reward2=[3, 4, 4, 5, 2], k=3))
