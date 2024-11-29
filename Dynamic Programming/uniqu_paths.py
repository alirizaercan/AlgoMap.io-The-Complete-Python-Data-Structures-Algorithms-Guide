class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top Down DP (Memoization)

        memo = {(0,0): 1}
        def paths(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif i<0 or j<0 or i==m or j==n:
                return 0
            else:
                val = paths(i,j-1) + paths(i-1,j)
                memo[(i,j)] = val
                return val

        return paths(m-1,n-1)

    # Time Complexity : O(m*n)
    # Space Complexity : O(m*n)