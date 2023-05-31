"""
1130.叶值的最小代价生成树
像哈夫曼树的构建过程。
单调栈。
"""


class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        while len(arr) > 1:
            index, minValue = -1, 272
            for i in range(0, len(arr) - 1):
                if arr[i] * arr[i+1] < minValue:
                    index = i
                    minValue = arr[i] * arr[i+1]
            # print(index)
            if index > -1:
                result += (arr[index] * arr[index+1])
                newValue = max(arr.pop(index), arr.pop(index))
                # print(newValue)
                arr.insert(index, newValue)
        return result
        """result = 0
        stack = []
        for x in arr:
            while stack and stack[-1] <= x:
                y = stack.pop()
                if not stack or stack[-1] > x:
                    result += y * x
                else:
                    result += stack[-1] * y
            stack.append(x)
        while len(stack) >= 2:
            x = stack.pop()
            result += stack[-1] * x
        return result"""


if __name__ == '__main__':
    sol = Solution()
    print(sol.mctFromLeafValues(arr=[15, 13, 5, 3, 15]))
