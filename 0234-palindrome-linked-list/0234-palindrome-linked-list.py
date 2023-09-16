# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverselist(self,head):
        current=head
        newlist=None

        while(current):
            next_node=current.next
            current.next=newlist
            newlist=current
            current=next_node
        return newlist
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast=slow=head

        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next    #find mid point

        temp1=self.reverselist(slow)
        temp2=head  

        while temp1 and temp2:
            if temp1.val!=temp2.val:
                return False
            temp1=temp1.next
            temp2=temp2.next
        return True
        
        