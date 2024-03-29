"""
143.重排链表
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        # 找分割点
        prev, slow, fast = head, head.next, head.next
        # 这里：当链表中节点个数为奇数时，fast 到达最后一个节点时，slow 到达分割点；
        # 当链表中节点个数为偶数时，fast 到达 None 节点时，slow 到达分割点。
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        head2 = slow
        # 反转后半段序列
        prev, slow, fast = None, head2, head2.next
        while slow:
            slow.next = prev
            if not fast:
                head2 = slow
            prev = slow
            slow = fast
            # 这里：最后一次反转时，slow 到达 None 节点，如果不加判断条件会报错
            fast = slow.next if slow else None
        # 拼接两段序列
        prev, slow, fast = head, head.next, head2
        while slow:
            # 这里：特别注意切换指针的顺序
            prev.next = fast
            fast = fast.next
            prev.next.next = slow
            slow = slow.next
            prev = prev.next.next
        while fast:
            prev.next = fast
            fast = fast.next
            prev = prev.next
        return head
