"""
617.合并二叉树
个人感觉和之前比较两棵树是否相同或对称是同一个逻辑。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeSubTree(node1, node2):
    if node1 is None:
        if node2 is None:
            return
        else:
            # 这里：可以想到的简化是，当两个节点中有一个为空时，直接返回另一个非空节点即可
            # 感觉还是利用了原来树上已有的节点，减少了递归的次数
            """root = TreeNode(val=node2.val)
            node1_left, node1_right = None, None
            node2_left, node2_right = node2.left, node2.right"""
            return node2
    else:
        if node2 is None:
            """root = TreeNode(val=node1.val)
            node1_left, node1_right = node1.left, node1.right
            node2_left, node2_right = None, None"""
            return node1
        else:
            root = TreeNode(val=node1.val + node2.val)
            root.left = mergeSubTree(node1.left, node2.left)
            root.right = mergeSubTree(node1.right, node2.right)
    return root


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return mergeSubTree(root1, root2)
