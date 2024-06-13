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
        拼接链表
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        # 在原始链表每个节点的后面拼接拷贝节点
        pointer = head
        while pointer:
            new_node = Node(x=pointer.val, next=pointer.next)
            pointer.next = new_node
            pointer = pointer.next.next
        # 根据原始链表调整拷贝节点的 random 指针
        pointer, new_pointer = head, head.next
        while pointer:
            new_pointer.random = pointer.random.next if pointer.random else None
            pointer = pointer.next.next
            new_pointer = pointer.next if pointer else None
        # 把两个链表拆分开
        new_head = head.next
        pointer, new_pointer = head, head.next
        while pointer.next.next:
            pointer.next = pointer.next.next
            new_pointer.next = new_pointer.next.next
            pointer = pointer.next
            new_pointer = new_pointer.next
        pointer.next = None
        return new_head
