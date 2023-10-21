class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorder_traverse(self, node, node_list):
        if not node:
            return
        self.inorder_traverse(node.left, node_list)
        node_list.append(node.val)
        self.inorder_traverse(node.right, node_list)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node_list = []
        self.inorder_traverse(root, node_list)
        for i in range(len(node_list)):
            if node_list[i] >= node_list[i + 1]:
                return False
        return True
