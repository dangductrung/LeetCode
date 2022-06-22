# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_top(self, newElement):
        newNode = ListNode(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseList = LinkedList()
        
        while head != None:
            reverseList.push_top(head.val)
            head = head.next
        return reverseList.head