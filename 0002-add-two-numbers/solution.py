# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1,v2 = 0,0
        c = 0
        if l1:
            v1 = l1.val 
        if l2:
            v2 = l2.val
        tempsum = v1+v2+c
        c= (tempsum)//10
        head = ListNode(tempsum%10)
        temp = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            a1 = l1.val
            a2 = l2.val
            total = a1+a2+c
            c = total//10
            head.next = ListNode(total%10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head = head.next
        while l1:
            a1 = l1.val
            a2 = 0
            total = a1+a2+c
            c = total//10
            head.next = ListNode(total%10)
            l1 = l1.next
            head = head.next
        
        while l2:
            a1 = 0
            a2 = l2.val
            total = a1+a2+c
            c = total//10
            head.next = ListNode(total%10)
            l2 = l2.next
            head = head.next
        if c>0:
            head.next = ListNode(c)
        return temp
