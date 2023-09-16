# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

         head1=l1
         head2=l2
         listans=ListNode() #creating linklist
         current=listans 
         carry=0

         #listans.append(head1.val+head2.val)
       
         while (head1 or head2 or carry):
            val1=head1.val if head1 else 0
            val2=head2.val if head2 else 0

            ans=(val1+val2+carry) #Total answer
            current.next=ListNode(ans%10) #1st digit
            carry=ans//10 #carry

            #print(listans)
            head1=head1.next if head1 else None #if head1<head2
            head2=head2.next if head2 else None #if head2<head1
            current=current.next

         return listans.next #we are starting from listans.next
