class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top Down DP (Memoization)
        m, n = len(text1), len(text2)
        
        @cache
        def longest(i,j):
            if i == m or j == n:
                return 0
            elif text1[i] == text2[j]:
                return 1 + longest(i+1,j+1)
            else:
                return max(longest(i,j+1), longest(i+1,j))
            
        return longest(0,0)

    # Time Complexity : O(m*n)
    # Space Complexity : O(m*n)