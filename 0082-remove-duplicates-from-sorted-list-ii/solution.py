# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        cur = dummy
        d = {}
        temp = head
        while temp:
            if temp.val in d:
                d[temp.val] += 1
            else:
                d[temp.val] = 1
            temp = temp.next

        while cur.next:
            if d[cur.next.val]>1 :
                cur.next = cur.next.next
            else:
                cur = cur.next  
        return dummy.next

