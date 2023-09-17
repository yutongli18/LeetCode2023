"""
222.完全二叉树的节点个数
完全二叉树的一个规律：只要顺着节点的左右孩子向下找，一定能找到一个子树，是满二叉树。
判断以某个节点为根的二叉树是否为满二叉树的方法：左子树的深度和右子树的深度相等。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkComplete(node):
    """ 判断以 node 为根节点的树是否为满二叉树 """
    left_depth, right_depth = 0, 0
    left_pointer, right_pointer = node, node
    while left_pointer is not None:
        left_depth += 1
        left_pointer = left_pointer.left
    while right_pointer is not None:
        right_depth += 1
        right_pointer = right_pointer.right
    return left_depth == right_depth, left_depth


def countSubNodes(node):
    num_nodes = 1
    check, depth = checkComplete(node)
    if check:
        return 2 ** depth - 1
    else:
        if node.left is not None:
            num_nodes += countSubNodes(node.left)
        if node.right is not None:
            num_nodes += countSubNodes(node.right)
        return num_nodes


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历：时间复杂度 O(n)
        """num_nodes = 0
        if root is None:
            return num_nodes
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            for i in range(len(traverse_list)):
                node = traverse_list.popleft()
                num_nodes += 1
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
        return num_nodes"""
        # 递归求和
        return countSubNodes(root)
