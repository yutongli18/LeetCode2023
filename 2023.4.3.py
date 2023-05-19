"""
1053.交换一次的先前排列
先找到最小的位置i，在此基础上找到最大的位置j，然后交换。
"""


class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arrLength = len(arr)
        for i in range(arrLength-2, -1, -1):
            if arr[i] > arr[i+1]:
                j = arrLength - 1
                while arr[j] >= arr[i] or arr[j] == arr[j-1]:
                    j -= 1
                # print(i, j)
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr[:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.prevPermOpt1(arr=[3, 1, 1, 3]))
