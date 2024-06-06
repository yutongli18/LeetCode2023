# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        21.合并两个有序链表
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        left, right = list1, list2
        head = None
        pre_node = None
        while left and right:
            if left.val <= right.val:
                # 拼接 left 对应的节点
                curr_node = left
                left = left.next
            else:
                curr_node = right
                right = right.next
            if not head:
                head = curr_node
            else:
                pre_node.next = curr_node
            pre_node = curr_node
        if left:
            if not head:
                head = left
            else:
                pre_node.next = left
        elif right:
            if not head:
                head = right
            else:
                pre_node.next = right
        return head
