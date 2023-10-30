class Solution(object):
    def deleteSub(self, node, key):
        if not node:
            return
        if node.val == key:
            # 当前节点就是目标节点
            if not node.left:
                if not node.right:
                    return
                else:
                    return node.right
            else:
                if not node.right:
                    return node.left
                else:
                    pointer = node.right
                    while pointer.left:
                        pointer = pointer.left
                    pointer.left = node.left
                    return node.right
        elif node.val > key:
            node.left = self.deleteSub(node.left, key)
        else:
            node.right = self.deleteSub(node.right, key)
        return node

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.deleteSub(root, key)
