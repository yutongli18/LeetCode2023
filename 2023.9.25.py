"""
113.路径总和II
和 112 题思路类似，但是不需要返回值了，因为是找所有的路径。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.path_list = []
        self.paths = []

    def getPath(self, node, count):
        count -= node.val
        self.path_list.append(node.val)
        if node.left is None and node.right is None:
            if count == 0:
                # 这里：必须写 self.path[:] 否则结果不能正常输出
                # 理解的话就是只传递值，不传递数组的引用本身，否则会随着 self.path_list 的变化而变化
                self.paths.append(self.path_list[:])
        if node.left is not None:
            self.getPath(node.left, count)
        if node.right is not None:
            self.getPath(node.right, count)
        count += node.val
        self.path_list.pop()
        return

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return self.paths
        self.getPath(root, targetSum)
        return self.paths
