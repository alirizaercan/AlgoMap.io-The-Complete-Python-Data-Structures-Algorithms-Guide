class Solution:
    def trap(self, height : List[int]) -> int:
        n = len(height)
        l = r = 0
        max_l = [0]*n
        max_r = [0]*n
        
        for i in range(n):
            j = -i-1
            max_l[i] = l
            max_r[j] = r
            l = max(l, height[i])
            r = max(r, height[j])
            
        summ = 0
        for i in range(n):
            pot = min(max_l[i], max_r[i])
            summ += max(0, pot - height[i])
            
        return summ
    
    # Time Complexity : O(n)
    # Space Complexity : O(n)