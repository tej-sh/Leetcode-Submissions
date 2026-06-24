# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stac = []
        cur = head
        while cur:
            stac.append(cur.val)
            cur = cur.next
        cur = head
        mx = float("-inf")
        while cur:
            mx = max(mx,cur.val+stac.pop())
            cur = cur.next
        return mx

        # st = head
        # rev = None
        # next = None
        # cur = head
        # while cur:
        #     next = cur.next 
        #     cur.next = rev
        #     rev = cur
        #     cur = next
        # mx = 0
        # while st:
        #     print(st.val)
        #     st = st.next
        # print("check rev")
        # while rev:
        #     print(rev.val)
        #     rev = rev.next
        
        # while st and rev:
        #     # print(st.val)
        #     # print(rev.val)
        #     mx = max(mx,st.val*rev.val)
        #     st = st.next
        #     rev = rev.next
        # return mx

