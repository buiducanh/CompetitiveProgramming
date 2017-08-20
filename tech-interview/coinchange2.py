from sys import stdin
def coinchange2(A,B):
    dp = [1 for i in xrange(B)]
    A = sorted(A)
    for i in range(0, B):
        for j in xrange(len(A)):
            if i+1- A[j] > 0 and dp[i-A[j]] > 0:
                dp[i] += dp[i-A[j]]
                break
            else:
                continue
    return dp[B-1]
inp = open("coinchange2.in", "r")
A = map(int, inp.readline().strip().split())
B = int(inp.readline())
print coinchange2(A,B)
