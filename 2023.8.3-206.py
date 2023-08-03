"""
206.反转链表
双指针法直接改变指针的指向
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = head
        right = head.next if head is not None else None
        while right is not None:
            after = right.next
            right.next = left
            if left.next == right:
                left.next = None
            left = right
            right = after
        return left