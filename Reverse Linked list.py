# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        c = ListNode()
        i = head
        while i:
            next = i.next
            i.next = c.next
            c.next = i
            i = next
        return c.next