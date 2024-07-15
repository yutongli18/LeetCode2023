from collections import deque


class Solution(object):
    def __init__(self):
        self.grid = []
        self.n = 0
        self.pre_count = []

    def canFinish(self, numCourses, prerequisites):
        """
        207.课程表
        类BFS
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[-1 for _ in range(numCourses)] for _ in range(numCourses)]
        pre_count = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            matrix[a][b] = 0
            pre_count[b] += 1
        queue = deque([])
        # 入度为0的课程入队
        for i in range(numCourses):
            if pre_count[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            for course in range(numCourses):
                if course != pre and matrix[pre][course] == 0:
                    pre_count[course] -= 1
                    if pre_count[course] == 0:
                        queue.append(course)
        # 有没有课程的入度不为0
        for count in pre_count:
            if count > 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(numCourses=8, prerequisites=[[1, 0], [0, 1]]))
