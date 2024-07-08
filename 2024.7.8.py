# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.count = 0
        self.curr_sum = 0
        self.sum_dict = {0: 1}

    def check_sum(self, node, target):
        """
        递归
        :param node: TreeNode
        :param target: int
        :return: list[int], list[int]
        """
        if not node:
            return
        self.curr_sum += node.val
        if self.sum_dict.get(self.curr_sum - target):
            self.count += self.sum_dict[self.curr_sum - target]
        self.sum_dict.setdefault(self.curr_sum, 0)
        self.sum_dict[self.curr_sum] += 1
        self.check_sum(node.left, target)
        self.check_sum(node.right, target)
        self.sum_dict[self.curr_sum] -= 1
        self.curr_sum -= node.val
        return

    def pathSum(self, root, targetSum):
        """
        437.路径总和 III
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.check_sum(root, targetSum)
        return self.count
