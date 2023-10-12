"""
98. 验证二叉搜索树
中序遍历 + 数组遍历
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidSubBST(node, lower, upper):
    # 判断当前的 node.val 是否合理
    if lower < node.val < upper:
        check_left, check_right = True, True
        if node.left is not None:
            new_lower, new_upper = lower, min(upper, node.val)
            check_left = isValidSubBST(node.left, new_lower, new_upper)
        if node.right is not None:
            new_lower, new_upper = max(lower, node.val), upper
            check_right = isValidSubBST(node.right, new_lower, new_upper)
        return check_left and check_right
    else:
        return False


def inorder(node, node_list):
    if node is None:
        return
    inorder(node.left, node_list)
    node_list.append(node.val)
    inorder(node.right, node_list)
    return node_list


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node_list = inorder(root, [])
        for i in range(len(node_list)):
            if node_list[i] >= node_list[i + 1]:
                return False
        return True
