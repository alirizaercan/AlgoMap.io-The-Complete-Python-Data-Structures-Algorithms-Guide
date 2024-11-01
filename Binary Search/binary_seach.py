class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while l<r:
            m = (l+r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                m = r-1
            else:
                m = l+1
                
        return -1
    
    # Time Complexity : O(log(n))
    # Space Complexity : O(1)