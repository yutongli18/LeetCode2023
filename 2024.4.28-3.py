class Solution(object):
    def minEnd(self, n, x):
        """
        100282.数组最后一个元素的最小值
        位运算。
        :type n: int
        :type x: int
        :rtype: int
        """
        # 数组 nums 应该从 x 开始构建，需要填充的元素个数应为 n - 1 个
        n -= 1
        # n 和 x 的移位
        n_step, x_step = 0, 0
        while n >> n_step:
            # 当 n 的位数没有被全部填充完时，需要继续填充
            while (x >> x_step) & 1 != 0:
                x_step += 1
            # 找到 x 中从左边数第一个 0 位，将 n 的当前位赋值给它
            x |= (n >> n_step & 1) << x_step
            x_step += 1
            # 继续赋 n 的下一位，直到赋完为止
            n_step += 1
        return x


if __name__ == '__main__':
    sol = Solution()
    print(sol.minEnd(n=3, x=4))
