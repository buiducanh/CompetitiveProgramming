class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for i in s]
        for i in range(len(s)):
            if '0' > s[i] or '9' < s[i]:
                return 0
            if i == 0:
                if '1' <= s[i] <= '9':
                    dp[i] = 1
            else:
                if '1' <= s[i] <= '9':
                    dp[i] = dp[i - 1]
                if 10 <= int(s[i - 1])*10 + int(s[i]) <= 26:
                    if i - 2 < 0:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i - 2]
        return dp[-1]
