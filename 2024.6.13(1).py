# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        138.随机链表的复制
        建立新老节点之间的映射。
        :type head: Node
        :rtype: Node
        """
        node_map = {}
        new_head = Node(x=-10**4-1)
        pre_node = new_head
        pointer = head
        while pointer:
            # 第一次遍历：拷贝节点，建立 next 指针关系，构建映射
            new_node = Node(x=pointer.val)
            node_map.setdefault(pointer, new_node)
            pre_node.next = new_node
            pre_node = new_node
            pointer = pointer.next
        pointer = head
        new_pointer = new_head.next
        while pointer:
            # 第二次遍历：根据映射构建 random 指针关系
            if pointer.random:
                new_pointer.random = node_map[pointer.random]
            pointer = pointer.next
            new_pointer = new_pointer.next
        return new_head.next
