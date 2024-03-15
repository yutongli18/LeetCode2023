"""
941.有效的山脉数组
"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # if len(arr) < 3:
        #     return False
        # top = max(arr)
        # top_index = arr.index(top)
        # if top_index <= 0 or top_index >= len(arr) - 1:
        #     return False
        # for i in range(1, top_index):
        #     if arr[i] <= arr[i - 1]:
        #         return False
        # for i in range(top_index + 1, len(arr)):
        #     if arr[i] >= arr[i - 1]:
        #         return False
        # return True
        if len(arr) < 3:
            return False
        # 双指针
        left, right = 0, len(arr) - 1
        while left < len(arr) - 1:
            if arr[left + 1] > arr[left]:
                left += 1
            else:
                break
        while right > 0:
            if arr[right] < arr[right - 1]:
                right -= 1
            else:
                break
        return 0 < left == right < len(arr) - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.validMountainArray(arr=[0, 3, 2, 1]))
