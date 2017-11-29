# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ext = 0
        node = ListNode(0)
        dummy = node
        while l1 or l2:
            sum = 0;
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += ext
            if sum/10 > 0 :
                ext = int(sum/10)
                node.next = ListNode(int(sum%10))
                node = node.next
            else:
                node.next = ListNode(sum)
                node = node.next
        if ext > 0:
            node.next = ListNode(ext)
        return dummy.next
        