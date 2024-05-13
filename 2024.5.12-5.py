# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        92.反转链表 II
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head.next or left == right:
            return head
        # 需要反转的部分的前一个节点
        pre_head = ListNode(next=head)
        # 用于反转的节点
        pre_ptr, curr_ptr, next_ptr = head, None, None
        # 用于记录遍历位置的变量
        position = 1
        while position < left:
            pre_head = pre_ptr
            pre_ptr = pre_ptr.next
            position += 1
        # 需要反转的链表的起始节点
        start = pre_ptr
        curr_ptr = pre_ptr.next
        next_ptr = pre_ptr.next.next if pre_ptr.next else None
        # 开始反转
        while position < right:
            curr_ptr.next = pre_ptr
            pre_ptr = curr_ptr
            curr_ptr = next_ptr
            next_ptr = next_ptr.next if next_ptr else None
            position += 1
        pre_head.next = pre_ptr
        start.next = curr_ptr
        return head if left > 1 else pre_head.next
