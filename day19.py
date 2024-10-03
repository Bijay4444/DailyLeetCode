"""70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases for when n is 1 or less
        if n == 1:
            return 1
        
        # Initialize the base cases
        dp = [0] * (n + 1)  # Create a list to store results for each step
        dp[0] = 1  # There's one way to stay on the ground (no steps)
        dp[1] = 1  # One way to take one step
        
        # Fill the dp array using the recurrence relation
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]  # The result is stored in dp[n]
  