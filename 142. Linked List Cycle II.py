# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def intersection(self, head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
        
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        intersect = self.intersection(head)
        
        if intersect == None:
            return None
        
        start = head
        while start != intersect:
            start = start.next
            intersect = intersect.next
        return start