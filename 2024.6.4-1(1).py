# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        234.回文链表
        空间复杂度 O(n)
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        pointer = head
        while pointer:
            stack.append(pointer)
            pointer = pointer.next
        # 判断
        pointer = head
        while pointer:
            node = stack.pop(-1)
            if node.val != pointer.val:
                return False
            pointer = pointer.next
        return True
