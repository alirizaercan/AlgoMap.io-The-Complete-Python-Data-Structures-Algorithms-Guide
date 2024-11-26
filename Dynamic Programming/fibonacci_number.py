# Top Down (Memoziation) Solution 
class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x+1) + f(x+2)
                return memo[x]

        return f(n)

    # Time Complexity : O(n)
    # Space Complexity : O(n)

    
# Bottom Up (Tabulation) Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    
# Bottom Up (Tabulation) Solution
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 :
            return 0
        if n == 1:
            return 1
        
        prev = 0
        cur = 1 
        
        for i in range(2,n+1):
            prev, cur = cur, prev+cur
            
        return cur
    
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    
# Fastest Approach
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1+(5**0.5)) / 2
        return int(round((golden_ratio**n)) / (5 ** 0.5))
    # Time Complexity : O(log(n))
    # Space Complexity : O(1)

    
