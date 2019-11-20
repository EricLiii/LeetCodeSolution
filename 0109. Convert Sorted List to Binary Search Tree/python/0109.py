# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
"""
Runtime: 136 ms, faster than 61.20% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 20.4 MB, less than 5.21% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return self.list_to_bst([head], 0, count-1)
    
    def list_to_bst(self, node_as_list, start, end):
        if start > end:
            return None
        mid = (start + end)//2
        # 注意以下操作的顺序不能乱。
        left_subtree = self.list_to_bst(node_as_list, start, mid-1)
        root = TreeNode(node_as_list[0].val)
        root.left = left_subtree
        node_as_list[0] = node_as_list[0].next
        root.right = self.list_to_bst(node_as_list, mid+1, end)
        return root
        
class Solution_2:
"""
Easier to understand and remember.

Runtime: 128 ms, faster than 88.25% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
Memory Usage: 17.6 MB, less than 52.08% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
"""
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            #利用slow和fast找中点的方法要学会！
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
    
