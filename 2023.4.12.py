"""
19.删除链表的倒数第N个结点
快慢双指针。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodeList = []
        length = 0
        currNode = head
        while currNode is not None:
            length += 1
            nodeList.append(currNode)
            currNode = currNode.next
        index = length - n
        if index >= 1:
            nodeList[index-1].next = nodeList[index].next
        else:
            head = nodeList[index].next
        del nodeList[index]
        return head
