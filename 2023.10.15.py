"""
501. 二叉搜索树中的众数
"""


from collections import Counter


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""def inorder_traverse(node, node_list):
    if node.left:
        inorder_traverse(node.left, node_list)
    node_list.append(node.val)
    if node.right:
        inorder_traverse(node.right, node_list)
    return node_list"""


def inorder_find(node, pre_node, mode_list, count, max_count):
    if node.left:
        pre_node, mode_list, count, max_count = inorder_find(node.left, pre_node, mode_list, count, max_count)
    if pre_node is None:
        pre_node = node.val
    if node.val == pre_node:
        count += 1
    else:
        count = 1
    pre_node = node.val
    if count == max_count:
        mode_list.append(node.val)
    elif count > max_count:
        mode_list = [node.val]
        max_count = count
    if node.right:
        pre_node, mode_list, count, max_count = inorder_find(node.right, pre_node, mode_list, count, max_count)
    return pre_node, mode_list, count, max_count


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """node_list = inorder_traverse(root, [])
        node_counter = Counter(node_list)
        count = node_counter[node_list[0]]
        mode = [node_list[0]]
        for value, counts in node_counter.items():
            if counts == count:
                mode.append(value)
            elif counts > count:
                mode = [value]
                count = counts
        return mode"""
        pre_node, mode_list, count, max_count = inorder_find(root, None, [], 0, 0)
        """if count == max_count:
            mode_list.append(pre_node)
        elif count > max_count:
            mode_list = [pre_node]"""
        return mode_list
