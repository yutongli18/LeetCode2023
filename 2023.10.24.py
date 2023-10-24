"""
77. 组合
递归 + 回溯
"""


class Solution(object):
    def __init__(self):
        self.combine_list = []

    def getSubCombine(self, n_list, k, pre_combine):
        if len(pre_combine) == k:
            self.combine_list.append(pre_combine)
            return
        # 这里：可以剪枝
        # 当剩余元素的个数不足以支持达成组成路径的条件时，可以直接把对应的树枝剪掉
        # 如果按照原来的条件继续遍历，会无法进入 for 循环而结束
        # for index in range(len(n_list)):
        for index in range(len(n_list) + len(pre_combine) - k + 1):
            # 这里：标准的回溯流程，在添加了该元素，递归完成之后，还需要把这个元素去除才行
            pre_combine.append(n_list[index])
            self.getSubCombine(n_list[index + 1:], k, pre_combine[:])
            pre_combine.pop(-1)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.getSubCombine(list(range(1, n + 1)), k, [])
        return self.combine_list
