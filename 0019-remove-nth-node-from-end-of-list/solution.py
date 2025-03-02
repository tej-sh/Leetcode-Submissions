# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #size with slow and fast -N/2
        #size-n - N
        #size
        p1 = head
        p2 = head
        s = 0
        while p1 is not None:
            s+=1
            p1 = p1.next

        if s==n:
            return head.next


        c = 0
        while p2 is not None and c < s-n-1 :
            p2 = p2.next
            c+=1
        p2.next = p2.next.next if p2.next is not None else None
        return head
