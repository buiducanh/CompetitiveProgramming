# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        def swapForward(prev, cur):
            if prev != cur: # cur is not head
                prev.next = cur.next
            next = cur.next
            cur.next = next.next
            next.next = cur
        if head.next:
            ans = head.next
            swapForward(head, head)
            head = ans
            cur = head.next.next
            prev = head.next
            while cur and cur.next:
                swapForward(prev, cur)
                prev = cur
                cur = cur.next
        return head
