class Solution(object):
    def __init__(self):
        self.mode_list = []
        self.max_freq = 0
        self.pre_value = - 10 ** 5 - 1
        self.curr_freq = 0

    def findSubMode(self, node):
        if not node:
            return
        # 左
        self.findSubMode(node.left)
        # 中
        if node.val == self.pre_value:
            self.curr_freq += 1
        else:
            self.curr_freq = 1
            self.pre_value = node.val
        if self.curr_freq > self.max_freq:
            self.mode_list = [node.val]
            self.max_freq = self.curr_freq
        elif self.curr_freq == self.max_freq:
            self.mode_list.append(node.val)
        # 右
        self.findSubMode(node.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.findSubMode(root)
        return self.mode_list
