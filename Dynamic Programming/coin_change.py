class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down Dynamic Programming (Memoization)

        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]

            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn, 1+min_coins(diff))

            memo[amt] = minn
            return minn

        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1

    # Time Complexity : O(coins*amount)
    # Space Complexity : O(amount)