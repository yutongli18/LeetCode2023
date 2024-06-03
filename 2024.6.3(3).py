# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_node(self, pre_node, node):
        if not node:
            return
        temp = node.next
        node.next = pre_node
        self.reverse_node(node, temp)

    def reverseList(self, head):
        """
        206.反转链表
        递归
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = head
        while pointer and pointer.next:
            pointer = pointer.next
        self.reverse_node(None, head)
        head = pointer
        return head
