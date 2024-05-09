class Solution(object):
    def countBits(self, num):
        """
        计算 num 二进制表示中 1 的数目。
        :type num: int
        :rtype: int
        """
        count_one = 0
        # for i in range(14):
        #     if num >> i & 1:
        #         count_one += 1
        # return count_one
        while num:
            num &= (num - 1)
            count_one += 1
        return count_one

    def sortByBits(self, arr):
        """
        1356.根据数字二进制下 1 的数目排序
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda num: [self.countBits(num), num])


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortByBits(arr=[2, 3, 5, 7, 11, 13, 17, 19]))
