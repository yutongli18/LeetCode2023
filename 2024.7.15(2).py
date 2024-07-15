class Solution(object):
    def __init__(self):
        self.grid = []
        self.n = 0
        self.pre_count = []

    def dfs_courses(self, pre):
        for course in range(self.n):
            if course != pre and self.grid[pre][course] == 0:
                self.pre_count[course] -= 1
                if self.pre_count[course] == 0:
                    self.dfs_courses(course)

    def canFinish(self, numCourses, prerequisites):
        """
        207.课程表
        DFS
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 初始化
        self.n = numCourses
        self.grid = [[-1 for _ in range(numCourses)] for _ in range(numCourses)]
        self.pre_count = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            self.grid[a][b] = 0
            self.pre_count[b] += 1
        start = []
        for i in range(numCourses):
            if self.pre_count[i] == 0:
                start.append(i)
        for i in start:
            self.dfs_courses(i)
        for count in self.pre_count:
            if count > 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(numCourses=8, prerequisites=[[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
