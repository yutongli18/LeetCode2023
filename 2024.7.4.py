# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        114.二叉树展开为链表
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        temp = root.right
        if root.left:
            root.right = self.flatten(root.left)
            # 把左子树上的节点挪到右子树上之后，必须把左指针清空，否则会有重复的问题
            root.left = None
            pointer = root.right
            while pointer.right:
                pointer = pointer.right
            pointer.right = self.flatten(temp)
        else:
            root.right = self.flatten(temp)
        return root
