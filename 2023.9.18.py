"""
110.平衡二叉树
思路没有问题，技巧上可以再优化。
递归的函数必须能够同时返回该二叉树的深度和该二叉树是否为平衡二叉树。
我的方法是返回两个参数，第一个是是否为平衡二叉树，第二个是该二叉树的深度，其实可以用一个参数表示。
如果返回二叉树的深度为 -1，表示已经为非平衡二叉树，就不需要做更多判断了。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""def checkBalanced(node, depth):
    depth += 1
    if node.left is not None:
        left_check, left_depth = checkBalanced(node.left, depth)
    else:
        left_check, left_depth = True, depth
    if node.right is not None:
        right_check, right_depth = checkBalanced(node.right, depth)
    else:
        right_check, right_depth = True, depth
    if not left_check or not right_check:
        return False, max(left_depth, right_depth)
    else:
        if abs(left_depth - right_depth) <= 1:
            return True, max(left_depth, right_depth)
        else:
            return False, max(left_depth, right_depth)"""


def getHeight(node):
    depth = 1
    if node is None:
        return 0
    left_depth = getHeight(node.left)
    right_depth = getHeight(node.right)
    if left_depth == -1 or right_depth == -1:
        return -1
    elif abs(left_depth - right_depth) <= 1:
        return depth + max(left_depth, right_depth)
    else:
        return -1


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """if root is None:
            return True
        check, depth = checkBalanced(root, 0)
        return check"""
        depth = getHeight(root)
        if depth < 0:
            return False
        else:
            return True
