# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        curr, prev = ListNode(head.val), None
        while head != None:
            curr = ListNode(head.val)
            curr.next = prev
            head = head.next
            prev = curr
        return curr
        
            