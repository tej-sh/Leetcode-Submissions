# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        do = ListNode(0)
        de = ListNode(0)
        c=1
        to =do
        te =de
        while(head is not None):
            if c%2 ==0:
                de.next = head
                de = de.next
            else:
                do.next = head
                do = do.next
            c+=1
            head = head.next
        de.next = None
        do.next = te.next
        
        return to.next

