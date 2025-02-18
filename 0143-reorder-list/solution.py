# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findmid(h):
            s,f = h,h
            while f.next is not None and f.next.next is not None:
                s = s.next
                f = f.next.next
            return s

        mid = findmid(head)
        sh = mid.next
        mid.next = None

        def rev(h):
            prev = None 
            while h is not None:
                temp = h.next
                h.next = prev
                prev = h
                h = temp
            return prev
        r = rev(sh)

        h1 = head
        h2 = r
        temp = h1

        while h1 is not None and h2 is not None:
            t1 = h1.next
            h1.next = h2
            t2 = h2.next
            h2.next = t1
            h1 = t1
            h2 = t2
        

            

