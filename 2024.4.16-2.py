class Solution(object):
    def countHurt(self, m, tower):
        count = 0
        num_row, num_col = len(m), len(m[0])
        for i in range(num_row):
            for j in range(num_col):
                if m[i][j] == '#':
                    for (x, y, r) in tower:
                        if abs(x - i) + abs(y - j) <= r:
                            count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    num_row, num_col, k = [int(num) for num in input().split(' ')]
    matrix = [[] for _ in range(num_row)]
    for i in range(num_row):
        matrix[i] = [ch for ch in input()]
    towers = []
    for i in range(k):
        tower = input().split(' ')
        towers.append([int(tower[0]) - 1, int(tower[1]) - 1, int(tower[2])])
    print(sol.countHurt(matrix, towers))
