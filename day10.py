"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        
        #pointers for traversing the list
        p1, p2 = list1, list2
        
        #traversing both lists and commpare nodes
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
                
            else:
                current.next = p2
                p2 = p2.next
                current = current.next
            
        #if any nodes are left in either list
        if p1:
            current.next = p1 
        if p2:
            current.next = p2
        
        #returns the merged list starting from the next of dummy node
        return dummy.next

