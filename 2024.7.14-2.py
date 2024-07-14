# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        """
        100368.从链表中移除在数组中存在的节点
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)
        # 按照链表的顺序把nums排序
        checked_nums = []
        dummy_head = ListNode(next=head)
        pointer = head
        while pointer:
            if pointer.val in nums_set:
                checked_nums.append(pointer.val)
            pointer = pointer.next
        # 按照顺序一次删除完成
        if len(checked_nums) <= 0:
            return dummy_head.next
        left = 0
        pointer = dummy_head
        while left < len(checked_nums):
            while pointer.next and pointer.next.val != checked_nums[left]:
                pointer = pointer.next
            if pointer.next:
                drop_pointer = pointer.next
                pointer.next = drop_pointer.next
                drop_pointer.next = None
                left += 1
            else:
                break
        return dummy_head.next
