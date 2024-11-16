from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        
        for key,val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
                
        return [h[1] for h in heap]
    
    # Time Complexity : O(nlog(k))
    # Space Complexity : O(k)