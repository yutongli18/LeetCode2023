"""
面试题02.07.链表相交
因为是从尾部开始算相等的，所以可以先把两个链表尾部对齐，然后从头开始判断
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointer_a, pointer_b = headA, headB
        length_a, length_b = 0, 0
        while pointer_a is not None:
            length_a += 1
            pointer_a = pointer_a.next
        while pointer_b is not None:
            length_b += 1
            pointer_b = pointer_b.next
        # 长度对齐
        # pointer_a 始终指向长度较短的那个序列
        if length_a < length_b:
            pointer_a, pointer_b = headA, headB
        else:
            pointer_a, pointer_b = headB, headA
        for _ in range(abs(length_a - length_b)):
            pointer_b = pointer_b.next
        # 开始找相交点
        while pointer_a is not None:
            if pointer_a != pointer_b:
                pointer_a = pointer_a.next
                pointer_b = pointer_b.next
            else:
                return f"Intersected at '{pointer_a.val}'"
        return None
