"""
450. 删除二叉搜索树中的节点
一共有 5 种情况，根据每种情况做单独讨论。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchDelete(self, node, key):
        if not node:  # 情况 ①
            return
        if node.val == key:
            if not node.left:  # 情况 ②
                if not node.right:
                    return
                else:  # 情况 ③
                    return node.right
            else:
                if not node.right:  # 情况 ③
                    return node.left
                else:  # 情况 ④
                    pre_node = node.right
                    while pre_node.left:
                        pre_node = pre_node.left
                    pre_node.left = node.left
                    return node.right
        if node.val > key:
            # 这里：其实不需要记录前一个节点和到底是左指针还是右指针
            # 只需要把新的节点返回，让上一层节点的左右节点来承接即可
            node.left = self.searchDelete(node.left, key)
        else:
            node.right = self.searchDelete(node.right, key)
        return node

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.searchDelete(root, key)
