# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        if not head or not head.next:
            return head

        pr = head.next

        prev = None

        while head and head.next is not None:
            first = head
            second = head.next

            first.next = second.next
            second.next = first
            if prev:
                prev.next = second

            prev = first
            head = first.next
            



        return pr
