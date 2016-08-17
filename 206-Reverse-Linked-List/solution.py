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
        fast_pointer = head
        new_list = ListNode(head.val)
        while fast_pointer.next:
            old_list = new_list
            fast_pointer = fast_pointer.next
            new_list = ListNode(fast_pointer.val)
            new_list.next = old_list
        return new_list
        