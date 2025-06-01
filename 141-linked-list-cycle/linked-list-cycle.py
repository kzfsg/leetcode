# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        def helper(head):
            if head == None:
                return False
            elif head in visited:
                return True
            else:
                visited.add(head)
                return helper(head.next)

        return helper(head)
        