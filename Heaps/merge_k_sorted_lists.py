import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
                
        D = ListNode()
        cur = D
        
        # nlog(k)
        while heap:
            val,i,node=heapq.heappop(heap)
            cur.next=node
            cur=node
            node=node.next 
            if node:
                heapq.heappush(heap,(node.val,i,node))
                
        return D.next 
    
    # Time Complexity : O(nlog(k))
    # Space Complexity : O(k)