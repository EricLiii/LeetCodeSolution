import heapq
class Solution:
"""
Runtime: 96 ms, faster than 96.82% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 16.5 MB, less than 48.48% of Python3 online submissions for Merge k Sorted Lists.

https://leetcode.com/problems/merge-k-sorted-lists/discuss/433087/Python-easy-and-fast-solution-using-min-heap-or-99
"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mylist = []
        head = ListNode('a')
        for l in lists:
            while l:
                mylist.append(l.val)
                l = l.next
        heapq.heapify(mylist) #记这个api
        temp = head
        while len(mylist):
            head.next = ListNode(heapq.heappop(mylist))
            head = head.next
        return temp.next