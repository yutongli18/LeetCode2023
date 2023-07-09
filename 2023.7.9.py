"""
707.设计链表
注意：
① 对于 index 不合法的判断，除了超出链表长度，还有本身数字不合法的情况
② addAtIndex 对 index 合法性的判断与其它不同，主要是因为可以插入到链表的尾部，改变链表的长度
③ 加入虚拟头节点之后，对 index 实际位置的判断要 + 1
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode()  # 伪头结点
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # index 不合法的可能情况有两种
        if index < 0 or index >= self.length:
            return -1
        pointer = self.head.next
        i = 0
        while i < index:
            pointer = pointer.next
            i += 1
        return pointer.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.length, val)  # 这里应该插入到 self.length 的位置上，而不是 self.length - 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # 节点可以被插入到链表的尾部，这里应该是严格 >
        # 只有插入有这种情况
        if index < 0 or index > self.length:
            return
        pointer = self.head  # 考虑到头插的可能性，这里应该从虚拟的头节点开始
        i = 0
        while i < index:  # 如果从虚拟的头节点开始计数，需要插入节点的位置是 index + 1
            pointer = pointer.next
            i += 1
        newNode = ListNode(val=val, next=pointer.next)
        pointer.next = newNode
        self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.length:
            return
        pointer = self.head  # 考虑到删除头节点的可能性，这里应该从虚拟的头节点开始
        i = 0
        while i < index:  # 从虚拟的头节点开始计数，需要删除节点的位置是 index + 1
            pointer = pointer.next
            i += 1
        pointer.next = pointer.next.next
        self.length -= 1
