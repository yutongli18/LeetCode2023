# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        24.两两交换链表中的节点
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(val=-1, next=head)
        pre_pointer, curr_pointer, next_pointer = dummy, head, head.next
        while next_pointer:
            # 交换节点
            pre_pointer.next = next_pointer
            curr_pointer.next = next_pointer.next
            next_pointer.next = curr_pointer
            # 更新指针
            pre_pointer = curr_pointer
            curr_pointer = curr_pointer.next
            next_pointer = curr_pointer.next if curr_pointer else None
        return dummy.next
