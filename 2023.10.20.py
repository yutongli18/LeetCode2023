"""
669. 修剪二叉搜索树
个人感觉比删除某个节点要简单，但是逻辑很相似。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimSubBST(self, node, low, high):
        if not node:
            return
        if node.val < low:
            # 这里：把右子树移上来之后，还需要对右子树进行修剪，不能直接返回
            # 因为右子树上也可能有不满足条件的节点
            return self.trimSubBST(node.right, low, high)
        elif node.val > high:
            return self.trimSubBST(node.left, low, high)
        else:
            # 这里：用返回值来实现删除节点的操作
            node.left = self.trimSubBST(node.left, low, high)
            node.right = self.trimSubBST(node.right, low, high)
            return node

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        return self.trimSubBST(root, low, high)
