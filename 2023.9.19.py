"""
257.二叉树的所有路径
递归 + 回溯
参数需要一个记录当前路径的列表和一个记录最终答案的列表
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getPath(node, path_list, paths):
    path_list.append(node.val)
    if node.left is None and node.right is None:
        paths.append("->".join([str(value) for value in path_list]))
        path_list.pop()
        return
    if node.left is not None:
        getPath(node.left, path_list, paths)
    if node.right is not None:
        getPath(node.right, path_list, paths)
    # 这里：当一个节点的两个子节点的路径都遍历完成之后，也应该要回溯了
    path_list.pop()
    return


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path_list, paths = [], []
        getPath(root, path_list, paths)
        return paths
