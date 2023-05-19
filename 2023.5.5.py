class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        maxId, maxTime = -1, 0
        for i in range(len(logs)):
            if i == 0:
                time = logs[i][1]
            else:
                time = logs[i][1] - logs[i-1][1]
            if time > maxTime:
                maxTime = time
                maxId = logs[i][0]
            elif time == maxTime:
                maxId = min(maxId, logs[i][0])
        return maxId


if __name__ == '__main__':
    sol = Solution()
    print(sol.hardestWorker(n=10, logs=[[0, 3], [2, 5], [0, 9], [1, 15]]))
