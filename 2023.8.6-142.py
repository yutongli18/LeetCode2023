class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast is None:  # 如果 fast 和 slow 指针没有会和，说明不存在环
            return None
        fast = head  # 把其中一个指针移动回开头
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
