"""
406.根据身高重建队列
贪心：先排高个子的，再排矮个子的
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: (p[0], -p[1]), reverse=True)
        queue = []
        for p in people:
            queue.insert(p[1], p[:])
        return queue


if __name__ == '__main__':
    sol = Solution()
    print(sol.reconstructQueue(people=[[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
