# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.recurSolution(lists, 0, len(lists) - 1)
        
    def merge(self, a, b):
        ans = ListNode(0)
        cur = ans
        while a and b:
            if a.val < b.val:
                cur.next = a
                cur = a
                a = a.next
            elif b.val <= a.val:
                cur.next = b
                cur = b
                b = b.next
        cur.next = a if a else b
        return ans.next
    
    def recurSolution(self, lists, start , end):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = start + (end - start + 1)/2
        return self.merge(self.recurSolution(lists, start, mid - 1), self.recurSolution(lists, mid, end))
