class Solution(object):
    def addToGraph(self, n, edges):
        group_a, group_b = [], []
        for u, v in edges:
            if u in group_a:
                group_b.append(v)
            elif u in group_b:
                group_a.append(v)
            else:
                group_a.append(u)
                group_b.append(v)
        return len(group_a) * len(group_b) - len(edges)


if __name__ == '__main__':
    n = int(input())
    edges = []
    i = 0
    while i < n - 1:
        edges.append([int(point) for point in input().split(" ")])
        i += 1
    sol = Solution()
    print(sol.addToGraph(n, edges[:]))
