class Solution:
    def countGood(self, a, b, c):
        """
        好评数
        :param a: list[int]
        :param b: list[int]
        :param c: list[int]
        :return: int
        """
        n, m = len(a), len(c)
        c.sort()
        # m 个人看帖子
        for j in range(m):
            # 看到每个帖子
            for i in range(n):
                if a[i] - b[i] >= c[j]:
                    a[i] += 1
                else:
                    b[i] += 1
        return sum([a[i] - b[i] for i in range(n)])


if __name__ == '__main__':
    n = int(input())
    a = [int(num) for num in input().split(' ')]
    b = [int(num) for num in input().split(' ')]
    m = int(input())
    c = [int(num) for num in input().split(' ')]
    sol = Solution()
    print(sol.countGood(a=a, b=b, c=c))
