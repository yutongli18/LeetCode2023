# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        206.反转链表
        O(n) 空间
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        pointer = head
        while pointer:
            stack.append(pointer)
            pointer = pointer.next
        head = stack[-1] if len(stack) > 0 else None
        while stack:
            node = stack.pop(-1)
            node.next = stack[-1] if len(stack) > 0 else None
        return head
