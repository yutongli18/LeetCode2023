"""
216. 组合总和 III
有更多条件的回溯。
注意递归时的传参。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []

    def getCombines(self, k, rest, start_index, curr_result):
        # 这里：用 k 来做终止条件
        # 用 rest 的话需要三重判断
        if k == 0:
            if rest == 0:  # 达成条件了，直接返回就行，没有必要再遍历下面的节点了
                self.result_list.append(curr_result)
            return
        for num in range(start_index, min(10, rest + 1, 11 - k)):  # 这里同时有两重剪枝可以做
            k -= 1
            rest -= num
            curr_result.append(num)
            # 这里：需要向下一层传递的应该是当前的 num 的下一个元素
            # 第一次整体逻辑对了，但是写成了 start_index + 1，所以从 2 往后的全都有重复……
            self.getCombines(k, rest, num + 1, curr_result[:])
            k += 1
            rest += num
            curr_result.pop(-1)

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.getCombines(k, n, 1, [])
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(k=9, n=45))
