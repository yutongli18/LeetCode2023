"""
203.移除链表元素
注意：① 虚拟头指针的作用；
② 如果单独用一个指针记录父亲的位置，记得更新这个指针
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        vHead = ListNode(next=head)  # 定义一个虚拟头结点
        pointer = vHead.next  # 遍历指针
        preNode = vHead  # 记录前一个位置
        while pointer is not None:
            if pointer.val == val:
                preNode.next = pointer.next
            else:  # 如果当前节点不删除，需要修改父指针的位置
                preNode = pointer
            pointer = pointer.next
        return vHead.next
