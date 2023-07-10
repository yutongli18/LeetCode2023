"""
206.反转链表
把自己绕进去了……
害怕反转指针下一个节点会丢失，直接用一个新的指针把下一个节点存起来就好了。
感觉受到双指针的影响都不敢做题了……

注意递归法要把最后的返回值一级一级传回最初的调用，所以每一轮调用都需要 return 返回。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """pre, cur, temp = None, head, None
        while cur is not None:
            temp = cur.next  # 担心改变指针方向之后下一个节点丢失，直接用一个指针记录这个节点即可
            cur.next = pre
            pre = cur
            cur = temp
        return pre"""
        def reverse(pre, cur):
            if cur is None:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)  # 这个地方必须也加上 return ，因为需要把返回的头节点一级一级传回最初的调用
        head = reverse(pre=None, cur=head)
        return head