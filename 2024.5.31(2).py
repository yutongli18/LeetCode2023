# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        160.相交链表
        双指针
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerA, pointerB = headA, headB
        lengthA, lengthB = 0, 0
        while pointerA:
            lengthA += 1
            pointerA = pointerA.next
        while pointerB:
            lengthB += 1
            pointerB = pointerB.next
        if lengthA >= lengthB:
            pointerA, pointerB = headA, headB
        else:
            pointerB, pointerA = headA, headB
        for _ in range(abs(lengthA - lengthB)):
            pointerA = pointerA.next
        while pointerA and pointerB:
            if pointerA == pointerB:
                return pointerA
            pointerA = pointerA.next
            pointerB = pointerB.next
        return None
