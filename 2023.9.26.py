"""
106. 从中序与后序遍历序列构造二叉树
注意：无论采取哪种遍历方式，左右子树的节点都不会混在一起，一定能找到一个分割点将属于左右子树的节点分割开
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createSubTree(inorder, postorder):
    # 后序遍历的最后一个元素是当前子树的根节点
    node_val = postorder[-1]
    postorder.pop()
    node = TreeNode(val=node_val)
    index = inorder.index(node_val)
    # 重新构建左右子树的中序和后序
    left_inorder = inorder[:index]
    right_inorder = inorder[index + 1:]
    # 这里：虽然一个是中序遍历，一个是后序遍历，但是左右子树的节点并不会混在一起
    # 换言之，知道了中序遍历左子树的节点个数 n ，那么后序遍历的前 n 个节点也一定来源于左子树，之后的节点一定来源于右子树
    left_postorder = postorder[:len(left_inorder)]
    right_postorder = postorder[len(left_inorder):]
    # 递归构建左右子树
    if len(left_inorder) > 0:
        node.left = createSubTree(left_inorder, left_postorder)
    if len(right_inorder) > 0:
        node.right = createSubTree(right_inorder, right_postorder)
    return node


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return createSubTree(inorder, postorder)
