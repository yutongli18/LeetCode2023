"""
111. 二叉树的最小深度
个人感觉层序遍历比递归好想到，代码也好写。
如果是层序遍历，只需要迭代遍历每一层节点，当该层某个节点为叶子节点时，返回当前的层数即可；注意每层开始遍历时要将层数加 1
如果是递归法，每轮递归的逻辑是，对于当前这个节点，如果有一个子节点不为空，说明当前节点不是叶子节点，需要顺着该子节点继续向下遍历；如果两个子节点都不为
空，需要在两棵子树的最小深度中选择更小的那一个；如果两个子节点都为空，说明该节点已经是叶子节点，最小层数即为该节点所处的层数，直接返回即可。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compareMinDepth(node, depth):
    """
    这个递归存在两个问题：
    1. 最小深度：只有两个子节点均为空的才是叶子节点，才有可能构成最小深度。所以当遇到一个子节点不为空的情况时，需要继续往下找。
    2. 因为把深度 depth 作为参数传递了，所以不需要每次求和，直接返回值即可
    """
    depth += 1
    if node.left is not None:
        if node.right is not None:
            depth = min(compareMinDepth(node.left, depth), compareMinDepth(node.right, depth))
        else:
            depth = compareMinDepth(node.left, depth)
    else:
        if node.right is not None:
            depth = compareMinDepth(node.right, depth)
    return depth


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """if root is None:
            return 0
        return compareMinDepth(root, 0)"""
        # 层序遍历
        min_depth = 0
        if root is None:
            return min_depth
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            min_depth += 1
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                if node.left is None:
                    if node.right is None:
                        return min_depth
                    else:
                        traverse_list.append(node.right)
                else:
                    if node.right is None:
                        traverse_list.append(node.left)
                    else:
                        traverse_list.append(node.left)
                        traverse_list.append(node.right)
