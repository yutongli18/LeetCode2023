import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        23.合并 K 个升序链表
        最小堆。
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for i in range(len(lists)):
            pointer = lists[i]
            while pointer:
                heapq.heappush(min_heap, pointer.val)
                pointer = pointer.next
        # 构建合并链表
        total_head = ListNode(val=-10 ** 4 - 1)
        pre_node = total_head
        while min_heap:
            val = heapq.heappop(min_heap)
            node = ListNode(val=val)
            pre_node.next = node
            pre_node = node
        return total_head.next
