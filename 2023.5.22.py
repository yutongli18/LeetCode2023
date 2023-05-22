"""
1080.根到叶路径上的不足节点
没办法记录前置节点的值，所以直接按照路径遍历。
DFS
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def checkSufficientLeaf(node, sum, limit):
            if node is None:
                return False
            if node.left is None and node.right is None:
                # 如果到达叶子节点，就计算路径的值
                return node.val + sum >= limit
            haveSufficientLeft = checkSufficientLeaf(node.left, sum + node.val, limit)
            haveSufficientRight = checkSufficientLeaf(node.right, sum + node.val, limit)
            if not haveSufficientLeft:
                node.left = None
            if not haveSufficientRight:
                node.right = None
            # 当两个子节点都是不足节点时，当前节点也是不足节点
            return haveSufficientLeft or haveSufficientRight
        haveSufficient = checkSufficientLeaf(root, 0, limit)
        return root if haveSufficient else None
