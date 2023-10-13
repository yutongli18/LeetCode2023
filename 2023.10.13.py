"""
530. 二叉搜索树的最小绝对差
中序遍历 + 指针记录上一个节点
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""def inorder_traverse(node, node_list):
    # 中序遍历
    if not node:
        return
    inorder_traverse(node.left, node_list)
    node_list.append(node.val)
    inorder_traverse(node.right, node_list)
    return node_list"""


def get_minimum_diff(node, pre_node, min_diff):
    if not node:
        return pre_node, min_diff
    pre_node, min_diff_left = get_minimum_diff(node.left, pre_node, min_diff)
    min_diff = min(min_diff, min_diff_left)
    if pre_node:
        min_diff = min(min_diff, abs(node.val - pre_node.val))
    pre_node = node
    pre_node, min_diff_right = get_minimum_diff(node.right, pre_node, min_diff)
    min_diff = min(min_diff, min_diff_right)
    return pre_node, min_diff


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """node_list = inorder_traverse(root, [])
        min_diff = node_list[1] - node_list[0]
        for i in range(1, len(node_list) - 1):
            min_diff = min(min_diff, node_list[i + 1] - node_list[i])
        return min_diff"""
        pre_node, min_diff = get_minimum_diff(root, None, 10 ** 5 + 1)
        return min_diff
