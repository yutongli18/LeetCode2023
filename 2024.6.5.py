# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        142.环形链表 II
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head
        # 先找是否有环
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and fast and slow == fast:
                break
        # 无环
        if not fast:
            return None
        # 有环，开始找入口
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
