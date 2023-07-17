"""
202. 快乐数
注意：
① 取一个数各位数的方法
② num_list 中的数必须一直保持，不能 pop 出来，因为 pop 出来的数字就不在 num_list 中了。
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_list = [n]
        while True:
            res = num_list[-1]
            result = 0
            while res != 0:
                result += (int(res % 10)) ** 2
                res = int(res / 10)
            if result == 1:
                return True
            elif result not in num_list:
                num_list.append(result)
            else:
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(n=2))
