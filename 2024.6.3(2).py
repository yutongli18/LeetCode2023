# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        206.反转链表
        迭代
        :type head: ListNode
        :rtype: ListNode
        """
        pre_pointer = None
        curr_pointer = head
        next_pointer = curr_pointer.next if curr_pointer else None
        while curr_pointer:
            curr_pointer.next = pre_pointer
            pre_pointer = curr_pointer
            curr_pointer = next_pointer
            next_pointer = curr_pointer.next if curr_pointer else None
        head = pre_pointer
        return head
