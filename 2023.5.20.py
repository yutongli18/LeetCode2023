"""
24.两两交换链表中的节点
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp1 = head
        if temp1 is None:
            return head
        temp2 = head.next
        if temp2 is None:
            return head
        preNode = None
        while temp1 is not None and temp2 is not None:
            print(temp1.val, temp2.val)
            if temp1 == head:
                head = temp2
            else:
                preNode.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1
            preNode = temp1
            temp1 = temp1.next if temp1.next is not None else None
            temp2 = temp1.next if temp1 is not None and temp1.next is not None else None
        return head