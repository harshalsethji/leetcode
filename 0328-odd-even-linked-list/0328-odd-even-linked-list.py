# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd_values = []
        even_values = []
        current = head
        index = 0
        
        while current:
            if index % 2 == 0:
                odd_values.append(current.val)
            else:
                even_values.append(current.val)
            current = current.next
            index += 1
        
        dummy = ListNode()
        current = dummy
        for val in odd_values + even_values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next