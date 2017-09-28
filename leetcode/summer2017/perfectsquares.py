class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        eps = 10**(-6)
        dp = [1 for i in range(n + 1)]
        for num in range(1, n + 1):
            if abs(int(num**(1/2.0)) - num**(1/2.0)) < eps:
                continue
            mink = n
            for k in range(1, int(num**(1/2.0) + 1)):
                if mink > 1 + dp[num - k*k]:
                    mink = 1 + dp[num - k*k]
            dp[num] = mink
        return dp[n]
