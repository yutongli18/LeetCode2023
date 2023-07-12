"""
19.删除链表的倒数第N个结点
快慢指针。
注意：快指针的速度是可以调整的，没必要拘泥于只比慢指针快 n-1 个单位，可以设置为 n + 1 个单位，这样慢指针正好能够指向需要删除结点的上一个结点。
"""


class ListNode(object):
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(next=head)
        left, right = dummy_head, dummy_head
        """for _ in range(n - 1):
            right = right.next"""
        for _ in range(n + 1):
            right = right.next
        """# 这里要保证 right 只能到达最后一个节点前的一个节点
        # right.next is not None 是保证 right 能到达最后一个节点
        while right.next.next is not None:
            left = left.next
            right = right.next"""
        while right is not None:
            left = left.next
            right = right.next
        # 要删除的是 left.next 位置的节点
        left.next = left.next.next
        return dummy_head.next

