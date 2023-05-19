"""
21.合并两个有序链表
可以通过添加一个头节点避开链表为空的检测。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode(val=-1)
        preNode = newList
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                preNode.next = list1
                list1 = list1.next
            else:
                preNode.next = list2
                list2 = list2.next
            preNode = preNode.next  # 个人感觉之前出错是在这个位置
        preNode.next = list1 if list1 is not None else list2
        return newList.next