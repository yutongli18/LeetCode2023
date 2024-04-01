"""
141.环形链表
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and fast and slow == fast:
                return True
        return False
