## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_list=None
        current=head
        

        while current:
            next_node=current.next # store next element
            current.next=new_list # rermove the arrow and point to previous one
            new_list=current # store current
            current=next_node # move to next

        return new_list # return head