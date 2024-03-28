"""
234.回文链表
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 先找分割点位置 split
        prev = head
        split, split2 = head, head
        while split2 and split2.next:
            prev = split
            split = split.next
            split2 = split2.next.next
        prev.next = None
        # 反转后半段字符串
        head2 = None  # 后半段的头节点
        prev, curr = None, split
        while curr:
            temp = curr.next
            curr.next = prev
            if not temp:
                head2 = curr
            prev = curr
            curr = temp
        # 按照前半段的长度，比较前后半段
        p1, p2 = head, head2
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
