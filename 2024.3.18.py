"""
1207. 独一无二的出现次数
哈希表
"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        curr_num = arr[0]
        curr_count = 1
        visited = [False for _ in range(1001)]
        for i in range(1, len(arr)):
            if arr[i] == curr_num:
                curr_count += 1
            else:
                if visited[curr_count]:
                    return False
                visited[curr_count] = True
                curr_num = arr[i]
                curr_count = 1
        if visited[curr_count]:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniqueOccurrences(arr=[1, 2]))
