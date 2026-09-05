# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 != None or l2 != None:
            if l1 != None:
                val1 = l1.val
            else:
                val1 = 0

            if l2 != None:
                val2 = l2.val
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            carry = total // 10
            total = total % 10

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
            current.next = ListNode(total)
            current = current.next

        if carry != 0:
            carry_node = ListNode(carry)
            current.next = carry_node
            
        return dummy.next