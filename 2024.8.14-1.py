class Solution(object):
    def __init__(self):
        self.min_stop = -1
        # 输入情况
        self.target = 0
        self.stations = []
        # 当前遍历情况
        self.curr_fuel = 0
        self.curr_stop = 0

    def dfsRefuel(self, i):
        self.curr_fuel -= (self.stations[i][0] - self.stations[i - 1][0])
        if i == len(self.stations) - 1 and self.curr_fuel >= 0:
            self.min_stop = min(self.min_stop, self.curr_stop) if self.min_stop >= 0 else self.curr_stop
        elif self.curr_fuel == 0:
            # 必须在当前加油站加油
            self.curr_fuel += self.stations[i][1]
            self.curr_stop += 1
            self.dfsRefuel(i + 1)
            self.curr_stop -= 1
            self.curr_fuel -= self.stations[i][1]
        elif self.curr_fuel > 0:
            # 如果在当前加油站加油
            self.curr_fuel += self.stations[i][1]
            self.curr_stop += 1
            self.dfsRefuel(i + 1)
            self.curr_stop -= 1
            self.curr_fuel -= self.stations[i][1]
            # 如果不在当前加油站加油
            self.dfsRefuel(i + 1)
        self.curr_fuel += (self.stations[i][0] - self.stations[i - 1][0])

    def minRefuelStops(self, target, start_fuel, stations):
        if start_fuel >= target:
            return 0
        if len(stations) <= 0 and start_fuel < target:
            return -1
        if start_fuel < stations[0][0]:
            return -1
        # 初始化
        self.target = target
        self.stations = [[0, 0]] + [[dis, fuel] for dis, fuel in stations] + [[target, 0]]
        self.curr_fuel = start_fuel
        # DFS
        self.dfsRefuel(1)
        return self.min_stop


if __name__ == "__main__":
    sol = Solution()
    print(sol.minRefuelStops(target=10, start_fuel=5, stations=[[5, 5]]))
