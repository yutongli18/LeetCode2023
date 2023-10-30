class Solution(object):
    def getPQ(self, node, p, q):
        if not node:
            return
        # 左
        left = self.getPQ(node.left, p, q)
        # 右
        right = self.getPQ(node.right, p, q)
        # 中
        # 这里：找 p 或 q 节点
        if node == p or node == q:
            return node
        else:
            # 这里：只要有返回值，就说明要么是找到了 p 或 q，要么是找到了最近公共祖先 node，直接返回就行了，不需要判断是哪种情况
            if not left:
                if not right:
                    return
                else:
                    return right
            else:
                if not right:
                    return left
                else:
                    return node

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.getPQ(root, p, q)
