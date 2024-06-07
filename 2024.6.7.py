# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        2.两数相加
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        left, right = l1, l2
        # 进位
        step = 0
        # 虚拟头节点
        dummy = ListNode(val=-1)
        pre_node = dummy
        while left and right:
            total = left.val + right.val + step
            node = ListNode(val=total % 10)
            pre_node.next = node
            step = total // 10
            left = left.next
            right = right.next
            pre_node = node
        if left:
            while left and step > 0:
                total = left.val + step
                node = ListNode(val=total % 10)
                pre_node.next = node
                step = total // 10
                left = left.next
                pre_node = node
            pre_node.next = left
        elif right:
            while right and step > 0:
                total = right.val + step
                node = ListNode(val=total % 10)
                pre_node.next = node
                step = total // 10
                right = right.next
                pre_node = node
            pre_node.next = right
        if step:
            pre_node.next = ListNode(val=step)
        return dummy.next
