# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        for i in range(k):
            current = head
            while current.next and current.next.next:
                current = current.next
            
            last_node = current.next
            current.next = None
            last_node.next = head
            head = last_node
        
        return head
                