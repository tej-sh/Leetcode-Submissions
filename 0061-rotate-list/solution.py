# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        temp = head
        size = 0
        while temp is not None:
            size+=1
            temp = temp.next
        
        moves = k%size
        if moves == 0:
            return head

        index = 0
        temp = head
        
        def move(prev):
            temp = prev
            while temp.next.next is not None:
                temp = temp.next
           
            last = temp.next
            temp.next = None
            last.next = prev

            return last

        for i in range(moves):
            head = move(head)
        
        return head
