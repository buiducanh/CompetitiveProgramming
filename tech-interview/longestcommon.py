def solve(s, t):
    m = len(s)
    n = len(t)
    dp = [[0 for i in xrange(n)] for j in xrange(m)]
    for id, i in enumerate(s):
        print id, i
        if i == t[0]:
            dp[id][0] = 1
        else:
            print id
            dp[id][0] = 0
    for id, i in enumerate(t):
        if i == s[0]:
            dp[0][id] = 1
        else:
            dp[0][id] = 0
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print dp[m-1][n-1]
    for i in dp:
        print
        for j in i:
            print j,

inp = open("longestcommon.in", "r")
s = inp.readline().strip()
t = inp.readline().strip()
solve(s,t)
