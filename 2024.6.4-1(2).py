# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        234.回文链表
        空间复杂度 O(1)
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return True
        # 前后段截断
        fast, slow = head, head
        pre_last = None
        while fast:
            pre_last = slow
            slow = slow.next
            fast = fast.next.next if fast.next else None
        pre_last.next = None
        head2 = slow
        # 后端翻转
        pre, curr, temp = None, head2, head2.next
        while curr:
            curr.next = pre
            pre = curr
            curr = temp
            temp = curr.next if curr else None
        head2 = pre
        # 前后段比较
        pointer1, pointer2 = head, head2
        while pointer2:
            if pointer1.val != pointer2.val:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return True
