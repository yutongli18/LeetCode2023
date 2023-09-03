from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result_list = []
        if root is None:
            return result_list
        traverse_queue = deque([root, None])
        # layer_list = []
        while len(traverse_queue) > 0:
            layer_list = []
            # 通过每层元素的个数做循环来判断当前层已经遍历完毕
            # for 循环一旦开始，traverse_queue 的长度变化不再影响遍历的次数
            for _ in range(len(traverse_queue)):
                node = traverse_queue.popleft()
                layer_list.append(node.val)
                if node.left is not None:
                    traverse_queue.append(node.left)
                if node.right is not None:
                    traverse_queue.append(node.right)
            result_list.append(layer_list)
            """node = traverse_queue.popleft()
            if node is None:  # 表示当前层已经遍历完毕
                result_list.append(layer_list)
                layer_list = []
                if len(traverse_queue) == 0:  # 当 traverse_queue 中只有一个 None 的时候，表示整个遍历流程结束
                    break
                else:
                    traverse_queue.append(None)  # 下一层的所有节点已经入队，添加一个分隔符
            else:
                layer_list.append(node.val)
                if node.left is not None:
                    traverse_queue.append(node.left)
                if node.right is not None:
                    traverse_queue.append(node.right)"""
        return result_list
