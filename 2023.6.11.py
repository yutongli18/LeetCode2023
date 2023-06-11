"""
1171.从链表中删去总和值为零的连续节点
如果两个节点有相同的前缀和，那么这两个节点之间的连续序列的和一定为零
对整个序列求和为零和头元素的值为零的情况需要一个特殊的技巧
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """newHead = ListNode(val=-1, next=head)
        prePointer = newHead
        pointer = head
        addSum = []  # （前置节点的指针，前缀和）
        while pointer is not None:
            if pointer.val == 0:
                prePointer.next = pointer.next
            else:
                for i in range(len(addSum)):
                    addSum[i][1] += pointer.val
                    if addSum[i][1] == 0:
                        addSum[i][0].next = pointer.next
                        prePointer = addSum[i][0]
                        addSum = addSum[:i]
                        break
                if prePointer.next == pointer:
                    addSum.append([prePointer, pointer.val])
                    prePointer = pointer
            pointer = pointer.next
        return newHead.next"""
        dummy = ListNode(val=0, next=head)
        prefix = 0
        seen = {0: dummy}
        while head is not None:
            prefix += head.val
            seen[prefix] = head  # 记录出现相同前缀和的最后位置
            head = head.next
        head = dummy  # 这个地方必须从dummy开始，否则无法解决第一个节点值为0的情况
        prefix = 0
        while head is not None:
            prefix += head.val
            head.next = seen[prefix].next  # 两个出现相同前缀和的位置之间的序列，和一定为0
            head = head.next
        return dummy.next