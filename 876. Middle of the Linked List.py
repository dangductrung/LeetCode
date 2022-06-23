# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        if (head.next).next == None:
            return head.next
        
        firstNode = head
        secondNode = (head.next).next
        
        while secondNode != None:
            if secondNode.next != None:
                if secondNode.next.next != None:
                    secondNode = secondNode.next.next
                else:
                    secondNode = secondNode.next
                firstNode = firstNode.next
            else:
                return firstNode.next
            
        return firstNode.next
                    
            
            
        