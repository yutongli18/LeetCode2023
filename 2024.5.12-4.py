# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        LCR 024.反转链表
        :type head: ListNode
        :rtype: ListNode
        """
        # 只有一个节点或没有节点
        if not head or not head.next:
            return head
        pre_head = ListNode(next=head)
        start, end = head, None
        pre_ptr, curr_ptr, next_ptr = head, head.next, head.next.next
        while curr_ptr:
            curr_ptr.next = pre_ptr
            pre_ptr = curr_ptr
            curr_ptr = next_ptr
            next_ptr = next_ptr.next if next_ptr else None
        pre_head.next = pre_ptr
        start.next = curr_ptr
        return pre_head.next

