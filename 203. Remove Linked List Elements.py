# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        while head.val == val:
            if head.next != None:
                head = head.next
            else:
                return None
        
        result = head
        start, end = result, result.next
        while end != None:
            if end.val == val:
                if end.next == None:
                    start.next = None
                    end = None
                else:
                    start.next = end.next
                    end = end.next
            else:
                start = start.next
                end = end.next    
            
        return result