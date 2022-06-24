# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start, end = head, head
        while end.next != None:
            if end.next.next != None:
                end = end.next.next
            else:
                end = end.next
            
            start = start.next
        return start