# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def remove_next(node):
            if node.next:
                node.next = node.next.next

        def iterator(node, n):
            if n == 0 or node == None:
                return node
            else:
                return iterator(node.next, n-1)

        dummy = ListNode(0)
        dummy.next = head

        # initiate pointers
        fast = iterator(dummy, n+1)
        slow = dummy

        if fast is None:
            return head.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        remove_next(slow)
        return head


        

        