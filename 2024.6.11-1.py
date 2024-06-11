# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        19.删除链表的倒数第 N 个结点
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1, head)
        pre, slow, fast = dummy_head, head, head
        for _ in range(n - 1):
            fast = fast.next
        while fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return dummy_head.next
