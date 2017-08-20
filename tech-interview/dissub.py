def print2d(a):
    for i in a:
        print
        for j in i:
            print j, 
    print
    
def solve(s, t):
    dp = [[0 for i in xrange(len(t))] for j in xrange(len(s))]
    if s[0] == t[0]:
        dp[0][0] = 1
    print2d(dp)
    for i in range(1, len(s)):
        if s[i] == t[0]:
            dp[i][0] = max(1, dp[i-1][0] + 1)
        else:
            dp[i][0] = dp[i-1][0]
    print2d(dp)
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if i < j:
                continue
            if s[i] == t[j]:
                if dp[i-1][j] != 0:
                    dp[i][j] = dp[i-1][j] + 1
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print2d(dp)
    return dp[len(s)-1][len(t)-1]

inp = open("dissub.in", "r")
s = inp.readline().strip()
t = inp.readline().strip()
print s, t
print solve(s,t)
