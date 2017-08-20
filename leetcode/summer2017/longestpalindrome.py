s = raw_input()

def longestPalindrome(s):
    if len(s) == 0:
        return ""

    dp = [[False for j in range(len(s) + 1)] for i in range(len(s))]

    for i in range(len(s)):
        dp[i][1] = True
        dp[i][0] = True

    res = s[0]
    for j in range(2, len(s) + 1):
        for i in range(j - 1, len(s)):
            if  s[i - j + 1] == s[i] and dp[i - 1][j - 2]:
                dp[i][j] = True
                if j > len(res):
                    res = s[i - j + 1: i + 1]
    return res

