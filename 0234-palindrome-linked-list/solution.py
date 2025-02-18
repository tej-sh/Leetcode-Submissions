# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def findmid(h):
            s,f = h,h
            while(f.next is not None and f.next.next is not None):
                s = s.next
                f = f.next.next
            return s
        t = head
        mid = findmid(head)
        sh = mid.next
        mid.next = None
        def reverse(h):
            prev = None
            while(h is not None):
                temp = h.next
                h.next = prev
                prev = h
                h = temp
            return prev
        rev = reverse(sh)
        while rev is not None and t is not None:
            if rev.val != t.val:
                return False
            rev = rev.next
            t = t.next
        return True

