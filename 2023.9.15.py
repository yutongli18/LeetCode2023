"""
559.N叉树的最大深度
"""


from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""def getDepth(node, depth):
    if node is None:
        return depth
    depth += 1
    maxDepth = 0
    for child in node.children:
        newDepth = getDepth(child, depth)
        maxDepth = newDepth if newDepth > maxDepth else maxDepth
    return maxDepth"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        """return getDepth(root, 0)"""
        depth = 0
        if root is None:
            return depth
        traverse_list = deque([root])
        while len(traverse_list) > 0:
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                for child in node.children:
                    if child is not None:
                        traverse_list.append(child)
            depth += 1
        return depth
