# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        141.环形链表
        空间复杂度：O(n)
        :type head: ListNode
        :rtype: bool
        """
        node_list = []
        pointer = head
        while pointer:
            if pointer not in node_list:
                node_list.append(pointer)
            else:
                return True
            pointer = pointer.next
        return False
