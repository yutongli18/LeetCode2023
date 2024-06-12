# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseGroupRecursive(self, head):
        """
        翻转链表
        递归
        :param head: ListNode
        :return: ListNode
        """
        if not head.next:
            return head
        new_head = self.reverseGroupRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseGroupIterative(self, head):
        """
        翻转链表（迭代）
        :param head: ListNode
        :return: ListNode
        """
        pre_pointer, curr_pointer, next_pointer = None, head, head.next
        while curr_pointer:
            curr_pointer.next = pre_pointer
            pre_pointer = curr_pointer
            curr_pointer = next_pointer
            next_pointer = curr_pointer.next if curr_pointer else None
        return pre_pointer

    def reverseKGroup(self, head, k):
        """
        25. K 个一组翻转链表
        分段
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(val=-1, next=head)
        # pre_tail：上一个分组的尾节点
        # seg_head：当前分组的头节点
        # pre_pointer: 当前分组的尾节点
        # pointer：下一个分组的头节点
        pre_tail, seg_head, pre_pointer, pointer = dummy, head, head, head
        while True:
            i = 0
            while i < k:
                if not pointer:
                    break
                pre_pointer = pointer
                pointer = pointer.next
                i += 1
            if i >= k:
                # 说明找到了一组
                pre_pointer.next = None
                pre_tail.next = self.reverseGroupIterative(seg_head)
                pre_tail = seg_head
                seg_head = pointer
                pre_pointer = pointer
            else:
                # 如果剩下的不够构成一组
                pre_tail.next = seg_head
                break
        return dummy.next
