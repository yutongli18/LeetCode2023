class Solution(object):
    def __init__(self):
        self.rooms = []
        self.visited = []

    def dfs(self, room_id):
        """
        DFS
        :type room_id: int
        :rtype: int
        """
        for id in self.rooms[room_id]:
            if self.visited[id]:
                continue
            self.visited[id] = True
            self.dfs(id)

    def canVisitAllRooms(self, rooms):
        """
        841.钥匙和房间
        DFS
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # 初始化
        n = len(rooms)
        self.rooms = rooms
        self.visited = [False for _ in range(n)]
        self.visited[0] = True
        # DFS
        self.dfs(0)
        # 判断
        for room_id in range(n):
            if not self.visited[room_id]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
