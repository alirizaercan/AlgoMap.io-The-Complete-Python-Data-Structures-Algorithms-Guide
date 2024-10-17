class Solution:
    def majorityElement(self, nums : List[int]) -> int:
        count_map = {}
        
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
                
        n = len(nums)
        for num, count in count_map.items():
            if count > n // 2:
                return num
            
        # Time Complexity : O(n)
        # Space Complexity : O(n)