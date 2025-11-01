# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = head
        while ans and ans.next:
            if ans.next.val == val:
                ans.next = ans.next.next
            else:
                ans = ans.next
        if head and head.val == val:
            return head.next if head.next else None
        return head if head else None
