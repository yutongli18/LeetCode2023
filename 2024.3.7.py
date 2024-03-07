"""
841.钥匙和房间
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 节点
        self.rooms = []
        # 是否遍历过
        self.visited = []

    # def dfs_visit(self, room_idx):
    #     if self.visited[room_idx]:
    #         return
    #     self.visited[room_idx] = True
    #     for next_idx in self.rooms[room_idx]:
    #         self.dfs_visit(next_idx)
    def bfs_visit(self):
        self.visited[0] = True
        queue = deque([0])
        while queue:
            room_idx = queue.popleft()
            for next_idx in self.rooms[room_idx]:
                if not self.visited[next_idx]:
                    self.visited[next_idx] = True
                    queue.append(next_idx)

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # 初始化
        self.rooms = [[key_idx for key_idx in room_idx] for room_idx in rooms]
        self.visited = [False for _ in range(len(rooms))]
        # 开始遍历
        # self.dfs_visit(room_idx=0)
        self.bfs_visit()
        # 检查每个房间是否都遍历到了
        for checked in self.visited:
            if not checked:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
