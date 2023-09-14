"""
101. 对称二叉树
递归法比较容易想到。
参数和返回值：两个树节点，布尔值
递归终止条件：树节点为 None 的情况，有四种
单层递归逻辑：递归的比较内层节点和外层节点是否相等
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare(node1, node2):
    if node1 is None:
        if node2 is None:
            return True
        else:
            return False
    else:
        if node2 is not None:
            if node1.val != node2.val:
                return False
            else:
                inner = compare(node1.right, node2.left)
                outer = compare(node1.left, node2.right)
                return inner and outer
        else:
            return False


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """traverse_list = deque([root])
        while len(traverse_list) > 0:
            layer_list = []
            for _ in range(len(traverse_list)):
                node = traverse_list.popleft()
                if node is not None:
                    layer_list.append(node.val)
                    traverse_list.append(node.left)
                    traverse_list.append(node.right)
                else:
                    layer_list.append(node)
            count = 0
            for i in range(len(layer_list)):
                if layer_list[i] is None:
                    count += 1
            if count == len(layer_list):
                break
            left, right = 0, len(layer_list) - 1
            while left < right:
                if layer_list[left] != layer_list[right]:
                    return False
                left += 1
                right -= 1
        return True"""
        """result_list = []
        traverse_list = [root]
        while len(traverse_list) > 0:
            node = traverse_list.pop()
            if node is not None:
                if node.right is not None:
                    traverse_list.append(node.right)
                traverse_list.append(node)
                traverse_list.append(None)
                if node.left is not None:
                    traverse_list.append(node.left)
            else:
                node = traverse_list.pop()
                result_list.append(node.val)
        left, right = 0, len(result_list) - 1
        while left < right:
            if result_list[left] != result_list[right]:
                return False
            left += 1
            right -= 1
        return True"""
        return compare(root.left, root.right)
