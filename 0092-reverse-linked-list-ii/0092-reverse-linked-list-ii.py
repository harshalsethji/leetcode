# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummylist = []
        current = head
        while current:
            dummylist.append(current.val)
            current = current.next

        left_index = left - 1
        right_index = right - 1
        
        dummylist[left_index:right_index + 1] = reversed(dummylist[left_index:right_index + 1])

        new_head = ListNode(dummylist[0])
        current = new_head
        
        for i in range(1, len(dummylist)):
            current.next = ListNode(dummylist[i])
            current = current.next
        
        return new_head