class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        
        
        if not nums:
            return ranges

        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i-1]}") 
                start = nums[i]
                
        if start == nums[-1]:
            ranges.append(str(start)) 
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        
        return ranges
    
    # Time Complexity : O(n)
    # Space Complexity : O(n)