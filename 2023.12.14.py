def complete_bag_problem(items, bag_size):
    """n = len(items)
    dp = [[0 for _ in range(bag_size + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, bag_size + 1):
            if j >= items[i - 1][0]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - items[i - 1][0]] + items[i - 1][1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]"""
    n = len(items)
    dp = [0 for _ in range(bag_size + 1)]
    for i in range(n):
        for j in range(items[i][0], bag_size + 1):
            dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])
    return dp[-1]


if __name__ == '__main__':
    n, bag_size = [int(num) for num in input().split()]
    items = []
    for i in range(n):
        weight, value = [int(num) for num in input().split()]
        items.append([weight, value])
    print(complete_bag_problem(items=items, bag_size=bag_size))
