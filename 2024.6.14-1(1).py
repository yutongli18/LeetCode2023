# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        148.排序链表
        模仿快排？模仿归并排序。
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            # 说明当前分段没有节点或只剩一个节点
            return head
        if not head.next.next:
            # 说明当前分段只剩两个节点，快慢指针找不到分割位置
            temp = head.next
            if head.val > temp.val:
                # 两个节点交换位置
                head.next = temp.next
                temp.next = head
                return temp
            return head
        # 说明当前分段的节点数大于 2
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 截断
        head2 = slow.next
        slow.next = None
        # 递归地去排序前后两个分段
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并前后两个有序分段
        dummy = ListNode(val=-10**5 - 1)
        pre_node = dummy
        pointer, pointer2 = head, head2
        while pointer and pointer2:
            if pointer.val <= pointer2.val:
                pre_node.next = pointer
                pre_node = pointer
                pointer = pointer.next
            else:
                pre_node.next = pointer2
                pre_node = pointer2
                pointer2 = pointer2.next
        if pointer:
            pre_node.next = pointer
        if pointer2:
            pre_node.next = pointer2
        return dummy.next
