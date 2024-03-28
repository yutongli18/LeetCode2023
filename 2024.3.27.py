"""
24.两两交换链表中的节点
双指针
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 设置虚拟头结点
        dummy_head = ListNode()
        dummy_head.next = head
        head = dummy_head
        p1 = dummy_head
        while p1 and p1.next and p1.next.next:
            p2, p3 = p1.next, p1.next.next
            p1.next = p3
            p2.next = p3.next
            p3.next = p2
            p1 = p1.next.next
        return head.next
