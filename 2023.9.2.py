"""
144. 二叉树的前序遍历
94. 二叉树的中序遍历
145. 二叉树的后序遍历
通用迭代法（标记法）：按照输出的顺序倒序入栈，当根节点入栈时，加入一个空指针（None）作为标记；当弹栈的是空指针时，将栈顶节点的值加入结果集合，否则继续入栈
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
        
        traverse_list = []
        result_list = []
        if root is not None:
            traverse_list.append(root)
        while len(traverse_list) > 0:
            node = traverse_list.pop()
            if node is not None:
                if node.right is not None:
                    traverse_list.append(node.right)
                if node.left is not None:
                    traverse_list.append(node.left)
                traverse_list.append(node)
                traverse_list.append(None)
            else:
                result_list.append(traverse_list.pop().val)
        return result_list"""


"""class Solution(object):
    def inorderTraversal(self, root):
        
        :type root: TreeNode
        :rtype: List[int]
        
        traverse_list = []
        result_list = []
        if root is not None:
            traverse_list.append(root)
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
                result_list.append(traverse_list.pop().val)
        return result_list"""


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traverse_list = []
        result_list = []
        if root:
            traverse_list.append(root)
        while traverse_list:
            node = traverse_list.pop()
            if node:
                traverse_list.append(node)
                traverse_list.append(None)
                if node.right:
                    traverse_list.append(node.right)
                if node.left:
                    traverse_list.append(node.left)
            else:
                result_list.append(traverse_list.pop().val)
        return result_list