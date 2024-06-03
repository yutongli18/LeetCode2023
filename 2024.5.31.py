# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        160.相交链表
        O(m + n) 的空间复杂度
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        tempA, tempB = headA, headB
        stackA, stackB = [], []
        while tempA:
            stackA.append(tempA)
            tempA = tempA.next
        while tempB:
            stackB.append(tempB)
            tempB = tempB.next
        temp = None
        while len(stackA) > 0 and len(stackB) > 0:
            nodeA = stackA.pop(-1)
            nodeB = stackB.pop(-1)
            if nodeA == nodeB:
                temp = nodeA
            else:
                return temp
        return temp
