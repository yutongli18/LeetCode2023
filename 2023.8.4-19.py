"""
19.删除链表的倒数第 N 个结点
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        left, right = dummy, dummy
        for _ in range(n + 1):
            right = right.next
        while right is not None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
