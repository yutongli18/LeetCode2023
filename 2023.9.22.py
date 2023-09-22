"""
404. 左叶子之和
思路没有问题，需要通过父节点判断当前节点是不是左叶子。
第一次提交的时候有个小问题，当当前节点的左节点不是叶子节点时，需要在这个左节点的子树上继续查找左叶子，不能不做处理，否则会丢失一些左叶子。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_left_sum(node):
    sub_sum = 0
    if node.left is not None:
        if node.left.left is None and node.left.right is None:
            sub_sum += node.left.val
        else:
            # 这里：如果当前节点的左节点不是叶子节点，那么要在这个左节点上继续查找左叶子，否则会少一些左叶子
            sub_sum += get_left_sum(node.left)
    if node.right is not None:
        sub_sum += get_left_sum(node.right)
    return sub_sum


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return get_left_sum(root)
