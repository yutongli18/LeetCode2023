"""
面试题02.07.链表相交
链表相交表示指向节点的指针相等。
因为指针相等，可以规避发现两个节点的值相等但是后续链表有不相等的情况。
感觉这个题目毫无技术含量，非常的扯……
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """a_stack, b_stack = [], []
        pointer = headA
        while pointer is not None:
            a_stack.append(pointer)
            pointer = pointer.next
        pointer = headB
        while pointer is not None:
            b_stack.append(pointer)
            pointer = pointer.next
        result = None
        while len(a_stack) > 0 and len(b_stack) > 0:
            a, b = a_stack.pop(-1), b_stack.pop(-1)
            if a != b:
                break
            else:
                result = a
        return result"""
        m, n = 0, 0
        pointer_a, pointer_b = headA, headB
        while pointer_a is not None:
            m += 1
            pointer_a = pointer_a.next
        while pointer_b is not None:
            n += 1
            pointer_b = pointer_b.next

        if m < n:  # pointer_a 指向较长的那个链表，m 指向较长的长度
            pointer_a = headB
            pointer_b = headA
            m, n = n, m
        else:
            pointer_a = headA
            pointer_b = headB
        for _ in range(m - n):
            pointer_a = pointer_a.next

        while pointer_a is not None and pointer_b is not None:
            if pointer_a == pointer_b:
                return pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        return None
