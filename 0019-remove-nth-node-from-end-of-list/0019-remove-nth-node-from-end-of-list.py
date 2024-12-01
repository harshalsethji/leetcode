# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listofnodes = []
        current = head
        while current:
            listofnodes.append(current.val)
            current = current.next
        
        listofnodes.pop(len(listofnodes) - n)
        
        if not listofnodes:
            return None
        
        dummy = ListNode(listofnodes[0])
        current = dummy
        for value in listofnodes[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return dummy
