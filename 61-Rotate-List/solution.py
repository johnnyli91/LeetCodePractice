# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
            
        copy_head = head
        slow_pointer = head
        fast_pointer = head
        length_linked_list = 0
        
        while copy_head:
            length_linked_list += 1
            copy_head = copy_head.next
            
        reduced_k = k % length_linked_list
        
        for i in xrange(reduced_k):
            if fast_pointer.next:
                fast_pointer = fast_pointer.next
            else:
                fast_pointer = head
        
        if fast_pointer == head:
            return head

        while fast_pointer and fast_pointer.next:
            if slow_pointer.next:
                slow_pointer = slow_pointer.next
            else:
                slow_pointer = head
            fast_pointer = fast_pointer.next
            print fast_pointer.val

        if slow_pointer.next:
            new_head = slow_pointer.next
            slow_pointer.next = None
        else:
            new_head = head

        if fast_pointer:
            fast_pointer.next = head
        return new_head
        
        