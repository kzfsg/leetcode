# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two non-empty linked lists
# two non-negative integers
# reverse order
# each node = single digit
# add both numbers and return the sum
# the lists are already in reverse order -> least signficant digit comes first -> propagate a carry-over

# 1. Walk both lists simultaneously. adding digits and carrying at each step
# 2. handle lists of unequal length by treating nodes as zero
# 3. after the loop, always check if there's leftover carry -> 999 + 1 = 1000


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # dummy node
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # loop
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+ val2 + carry

            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            # advance 
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        
        