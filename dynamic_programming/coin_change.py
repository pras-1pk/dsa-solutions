class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """Return the fewest number of coins needed to make up the given amount.

        Approach:
        - dp[a] = minimum number of coins to make amount a
        - initialize dp[0] = 0 and dp[1..amount] = infinity
        - for each amount a from 1 to amount, try every coin c:
          if a >= c, update dp[a] = min(dp[a], dp[a-c] + 1)

        Time: O(n * amount), where n = len(coins)
        Space: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != float('inf') else -1
    
    # Follow up : What changes if each coin can only be used once (0/1 knapsack)?
    #             How do you reconstruct which coins were used?
