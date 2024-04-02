"""
LCR 023.相交链表
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 遍历第一次，找到两个单链表的长度
        a_length, b_length = 0, 0
        a_p, b_p = headA, headB
        while a_p:
            a_length += 1
            a_p = a_p.next
        while b_p:
            b_length += 1
            b_p = b_p.next
        # 从尾部开始对齐两个单链表
        a_p, b_p = headA, headB
        if a_length > b_length:
            for _ in range(a_length - b_length):
                a_p = a_p.next
        elif a_length < b_length:
            for _ in range(b_length - a_length):
                b_p = b_p.next
        # 现在开始找相交的节点
        while a_p and b_p:
            if a_p == b_p:
                return a_p
            a_p = a_p.next
            b_p = b_p.next
        return None
