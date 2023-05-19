"""
1019.链表中的下一个更大节点
单调栈：栈中的元素非单调递减。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        """
        # 直接遍历
        currNode = head
        resultList = []
        while currNode is not None:
            checkNode = currNode.next
            while checkNode is not None:
                if checkNode.val > currNode.val:
                    resultList.append(checkNode.val)
                    break
                else:
                    checkNode = checkNode.next
            if checkNode is None:
                resultList.append(0)
            currNode = currNode.next
        return resultList
        """
        answerList = []
        currNode = head
        traverseList = []  # 存放元组(Node, index)
        index = -1
        while currNode is not None:
            index += 1
            answerList.append(0)
            while len(traverseList) > 0 and currNode.val > traverseList[-1][0].val:  # 大于栈顶元素则出栈
                answerList[traverseList[-1][1]] = currNode.val
                traverseList.pop(-1)
            traverseList.append((currNode, index))  # 存放两个元素：节点和索引
            currNode = currNode.next
        return answerList
