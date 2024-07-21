class Solution(object):
    def get_two(self, n):
        """
        获得n的二进制数组
        :param n: int
        :return: int[]
        """
        rest = n
        two_list = []
        while rest > 0:
            two_list.append(rest % 2)
            rest = rest // 2
        return two_list[:]

    def minChanges(self, n, k):
        """
        100372.使两个整数相等的位更改次数
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        n_list, k_list = self.get_two(n), self.get_two(k)
        if len(k_list) > len(n_list):
            return -1
        i = 0
        while i < min(len(n_list), len(k_list)):
            if n_list[i] == 1 and k_list[i] == 0:
                count += 1
            elif n_list[i] == 0 and k_list[i] == 1:
                return -1
            i += 1
        while i < len(n_list):
            if n_list[i] == 1:
                count += 1
            i += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.minChanges(n=54, k=25))
