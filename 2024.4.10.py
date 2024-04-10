# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.total = 0
        self.current = 0

    def dfs(self, node):
        # 这种写法有两处都需要回溯
        # 当到达叶子节点时和当前节点的左右子树遍历完毕时
        self.current *= 10
        self.current += node.val
        if not node.left and not node.right:
            self.total += self.current
            self.current -= node.val
            self.current /= 10
            return
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)
        self.current -= node.val
        self.current /= 10

    def sumNumbers(self, root):
        """
        129.求根节点到叶节点的数字之和
        :type root: TreeNode
        :rtype: int
        """
        self.current = root.val
        self.dfs(root)
        return self.total
