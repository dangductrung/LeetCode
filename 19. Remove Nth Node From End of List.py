# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        result = head
        start, end = result, result

        count = 1
        
        while count <= n:
            end = end.next
            count += 1
            
        if end == None:
            return head.next
        
        while end.next != None:
            start = start.next
            end = end.next
        
        start .next = start.next.next
        
        return result
        