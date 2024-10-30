# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        placeholder = ListNode()
        placeholder.next = head
        slow = fast = placeholder
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            
            if slow is fast:
                return True
            
        return False
    
    # Time Complexity : O(n)
    # Space Complexity : O(1)