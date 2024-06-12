# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        24.两两交换链表中的节点
        递归法
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp
