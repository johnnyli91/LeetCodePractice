# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        new_list = ListNode(head.val)
        while head.next:
            old_list = new_list
            head = head.next
            new_list = ListNode(head.val)
            new_list.next = old_list
        return new_list
        