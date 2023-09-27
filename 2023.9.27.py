"""
105. 从前序与中序遍历序列构造二叉树
做这道题的时候思考了一下，想要构造唯一的二叉树，必须要有中序遍历的序列。
因为只靠前序遍历和后序遍历，是没法区分左右子树上的节点的，必须要有一个根节点在中间的中序遍历，才能把两棵子树上的节点分开。
所以前序+中序或后序+中序都能构造二叉树，方法几乎是一模一样的，只不过一个根节点在最前面，一个根节点在最后面。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildSubTree(preorder, inorder):
    # 先序遍历的第一个节点是根节点
    root = TreeNode(val=preorder[0])
    index = inorder.index(preorder[0])
    preorder.pop(0)
    # 构建左右子树的中序遍历
    left_inorder = inorder[:index]
    right_inorder = inorder[index + 1:]
    left_length = len(left_inorder)
    # 构建左右子树的先序遍历
    left_preorder = preorder[:left_length]
    right_preorder = preorder[left_length:]
    # 递归构建左右子树
    if left_length > 0:
        root.left = buildSubTree(left_preorder, left_inorder)
    if len(right_inorder) > 0:
        root.right = buildSubTree(right_preorder, right_inorder)
    return root


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return buildSubTree(preorder, inorder)
