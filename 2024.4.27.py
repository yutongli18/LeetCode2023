# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def __init__(self):
        self.depth = 0
        self.preList = []

    def pre_order(self, node):
        if not node:
            return
        if self.depth == len(self.preList):
            # 说明第 depth 层还没有过节点
            self.preList.append(node)
        else:
            # 说明第 depth 层有前置节点，就把 next 指针连接一下
            self.preList[self.depth].next = node
            self.preList[self.depth] = node
        # 要进入下一层了，层深度增加
        self.depth += 1
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)
        # 要返回上一层了，层深度减少
        self.depth -= 1

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.pre_order(root)
        return root
