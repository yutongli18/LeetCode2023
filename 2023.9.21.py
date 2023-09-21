"""
572.另一棵树的子树
本质上和判断两棵树是否相同没有区别，只不过把根节点变成了树的中间节点。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compareNode(node1, node2):
    if node1 is None:
        if node2 is None:
            return True
        else:
            return False
    else:
        if node2 is None:
            return False
        else:
            if node1.val != node2.val:
                return False
            return compareNode(node1.left, node2.left) and compareNode(node1.right, node2.right)


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                if node.val == subRoot.val:
                    if compareNode(node, subRoot):
                        return True
                if node.left is not None:
                    traverse_list.append(node.left)
                if node.right is not None:
                    traverse_list.append(node.right)
        return False
