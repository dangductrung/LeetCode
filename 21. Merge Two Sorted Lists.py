# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push_back(self, newElement):
        newNode = ListNode(newElement)
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
            
    def push_list_back(self, list):
        while list != None:
            self.push_back(list.val)
            list = list.next
        
    def get_list_value(self) -> [int]:
        temp = self.head
        result = []
        while(temp != None):
            result.append(temp.val)
            temp = temp.next
        return result
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = LinkedList()
        result = []
        while list1 != None or list2 != None:
            if list1 == None:
                list.push_list_back(list2)
                list2 = None
            elif list2 == None:
                list.push_list_back(list1)
                list1 = None
            elif list1.val > list2.val:
                list.push_back(list2.val)
                list2 = list2.next
            else:
                list.push_back(list1.val)
                list1 = list1.next
        return list.head