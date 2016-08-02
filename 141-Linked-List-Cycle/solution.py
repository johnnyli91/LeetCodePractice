# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast_pointer = head
        slow_pointer = head
        try:
            while fast_pointer.next and slow_pointer.next.next:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next.next
                if fast_pointer == slow_pointer:
                    return True
        except AttributeError:
            return False
        return False
        
        