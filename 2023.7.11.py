"""
24.两两交换链表中的节点
注意：
除了交换两个节点的指针方向之外，还需要对上一个节点的指针指向进行修正。
"""


class ListNode(object):
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(next=head)
        preNode = dummyHead
        left = head
        right = left.next if left is not None else None
        while right is not None:
            # 交换
            left.next = right.next
            right.next = left
            # 更新上一个节点的指向
            preNode.next = right
            # 更新指针的值
            preNode = left
            left = left.next
            right = left.next if left is not None else None
        return dummyHead.next