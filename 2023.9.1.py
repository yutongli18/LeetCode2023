"""
144. 二叉树的前序遍历
94. 二叉树的中序遍历
145. 二叉树的后序遍历
迭代法。
关键：入栈的顺序和处理的顺序是否相同。
对于前序遍历，根节点先入栈，也先处理根节点（这里只是输出），所以先弹栈，再左右节点入栈；
对于中序遍历，根节点先入栈，但先处理最左边的节点，所以先入栈到没有左节点为止，然后出栈（相当于是根节点），再去查找右节点的情况。
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""class Solution(object):
    def preorderTraversal(self, root):
        
        :type root: TreeNode
        :rtype: List[int]
        
        result = []
        if root is None:
            return result
        traverse_stack = [root]
        while traverse_stack:
            node = traverse_stack.pop()
            result.append(node.val)
            if node.right:  # 空节点不入栈
                traverse_stack.append(node.right)
            if node.left:
                traverse_stack.append(node.left)
        return result"""


"""class Solution(object):
    def inorderTraversal(self, root):
    
        :type root: TreeNode
        :rtype: List[int]
        
        result = []
        traverse_list = []
        node = root
        while node is not None or len(traverse_list) > 0:
            if node is not None:  # 先找到整个二叉树最左边的节点
                traverse_list.append(node)
                node = node.left
            else:
                node = traverse_list.pop()  # 中
                result.append(node.val)
                node = node.right  # 右
        return result"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        traverse_list = [root]
        while len(traverse_list) > 0:
            node = traverse_list.pop()
            result.append(node.val)
            if node.left is not None:
                traverse_list.append(node.left)
            if node.right is not None:
                traverse_list.append(node.right)
        result.reverse()
        return result
