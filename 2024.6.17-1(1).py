# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeLists(self, list1, list2):
        """
        合并两个升序链表。
        :param list1: List[ListNode]
        :param list2: List[ListNode]
        :return: ListNode
        """
        if not list1:
            return list2
        if not list2:
            return list1
        head = ListNode(val=-10 ** 4 - 1)
        pre_node = head
        pointer1, pointer2 = list1, list2
        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                pre_node.next = pointer1
                pre_node = pointer1
                pointer1 = pointer1.next
            else:
                pre_node.next = pointer2
                pre_node = pointer2
                pointer2 = pointer2.next
        if pointer1:
            pre_node.next = pointer1
        if pointer2:
            pre_node.next = pointer2
        return head.next

    def mergeKLists(self, lists):
        """
        23.合并 K 个升序链表。
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) <= 0:
            return None
        total_head = None
        for i in range(len(lists)):
            total_head = self.mergeLists(total_head, lists[i])
        return total_head
