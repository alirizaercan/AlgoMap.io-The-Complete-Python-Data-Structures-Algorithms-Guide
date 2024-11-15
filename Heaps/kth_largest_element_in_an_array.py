import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i] # Max Heap
            
        heapq.heapify(nums)
        
        for _ in range(k-1):
            heapq.heappop(nums)
            
        return -heapq.heappop(nums)
            # Max Heap of size n
    # Time Complexity : O(n+klog(n))
    # Space Complexity : O(1)