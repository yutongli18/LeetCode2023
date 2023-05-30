"""def DFS(root, value):

    深度优先遍历
    :param root: 当前遍历的根节点
    :param value: 需要查找的值
    :return: 指向查找结果的指针

    if root is None:
        return None
    if root.val == value:
        return root
    pointer = DFS(root.left, value)
    if pointer is not None:
        return pointer
    pointer = DFS(root.right, value)
    if pointer is not None:
        return pointer
    if root is None or (root.left is None and root.right is None):
        return None, None, -1
    if root.val == value:
        return None, root, -1
    if root.left is not None and root.left.val == value:
        return root, root.left, 0
    if root.right is not None and root.right.val == value:
        return root, root.right, 1
    preNode, node, child = DFS(root.left, value)
    if node is not None:
        return preNode, node, child
    preNode, node, child = DFS(root.right, value)
    if node is not None:
        return preNode, node, child


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        roots = [root]
        for index in to_delete:
            preNode, node, child, subRoot = None, None, 0, None
            for newRoot in roots:
                node = DFS(newRoot, index)
                if node is not None:
                    roots.remove(newRoot)
                    subRoot = newRoot
                    break
            if node is not None:
                if node.left is not None:
                    roots.append(node.left)
                if node.right is not None:
                    roots.append(node.right)
                if subRoot is not None:
                    roots.append(subRoot)
        return roots
            for newRoot in roots:
                preNode, node, child = DFS(newRoot, index)
                if node is not None:
                    roots.remove(newRoot)
                    subRoot = newRoot
                    break
            if node is not None:
                if node.left is not None:
                    roots.append(node.left)
                if node.right is not None:
                    roots.append(node.right)
                if child == 0:
                    preNode.left = None
                elif child == 1:
                    preNode.right = None
                if preNode is not None:
                    roots.append(subRoot)
        return roots"""
"""
1110.删点成林
遇到的问题：
1.如何删除节点：需要把它的父节点的对应孩子指针设置为None，可以一边进行DFS遍历一边将对应节点设置为None，就不需要记录对应的父节点了；
2.如何添加新根节点：用一个符号位。如果父节点被删除了，它的两个孩子节点都有成为新根节点的潜质。
"""


def dfs(node, isRoot, toDeleteSet, roots):
    if node is None:
        return None
    delete = node.val in toDeleteSet  # 判断当前节点是否需要删除
    node.left = dfs(node.left, delete, toDeleteSet, roots)  # 如果当前节点需要删除，那么它的孩子节点有成为新根节点的潜质
    node.right = dfs(node.right, delete, toDeleteSet, roots)
    if delete:  # 如果当前节点需要删除的话，它的父节点的对应孩子指针会变成None
        return None
    else:
        if isRoot:  # 如果当前节点不需要删除，它又有成为新根节点的潜质（父节点被删除了），将它添加根节点的集合中
            roots.append(node)
        return node


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        toDeleteSet = set(to_delete)
        roots = []
        dfs(root, True, toDeleteSet, roots)
        return roots
