"""
142.环形列表II
快慢指针 + 数学
注意：
① 快指针每次走两个节点，慢指针每次走一个节点，如果快慢指针能够相遇，则证明链表中有环；
② 设链表头节点到环形入口点的节点数为 x，环形入口点到相遇点的节点数为 y，相遇点回到环形入口点的节点数为 z：
则到快慢指针相遇时，快节点共走了 x + n * (y + z) + z 个节点，慢指针共走了 x + z 个节点；
因为快指针每次走两个节点，所以 x + n * (y + z) + z = 2 * (x + z)；
化简得到： x = (n - 1)(y + z) + z;
当 n = 1 时， x = z，说明环形入口点的位置等价于两个节点，一个从头节点出发，一个从相遇点出发，最后相遇的地方。
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                fast = head  # slow 指针定在相遇点上，fast 指针回到开头
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
