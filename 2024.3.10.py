"""
100233.重新分装苹果
"""


class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total = sum(apple)
        capacity.sort(reverse=True)
        count = 0
        while total > 0:
            total -= capacity[count]
            count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumBoxes(apple=[1, 3, 2], capacity=[4, 3, 1, 5, 2]))
