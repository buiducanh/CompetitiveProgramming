class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.matchRecur(s, p, 0, 0)

    def matchDP(self, s, p):
        dp = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = True

        for i in range(len(s) + 1):
            dp[i][0] = True

    def matchRecur(self, s, p, si, pi):
        if (0 > si or si > len(s)) or (0 > pi or pi > len(p)):
            return False

        if si == len(s):
            jumps = 0
            while pi + jumps + 1 < len(p) and p[pi + jumps + 1] == '*':
                jumps += 2

            if pi + jumps == len(p):
                return True

            return False
        else:
            if pi == len(p):
                return False

            if pi + 1 < len(p) and p[pi + 1] == '*':
                return (self.matchRecur(s, p, si, pi + 2) or
                       (p[pi] == '.' or s[si] == p[pi]) and
                       self.matchRecur(s, p, si + 1, pi))
            else:
                return ((p[pi] == '.' or s[si] == p[pi]) and
                       self.matchRecur(s, p, si + 1, pi + 1))
    def dpOrRecur(self, s, p, si, pi):
        if self.dp[si][pi] == -1:
            self.dp[si][pi] = self.matchRecur2(s, p, si, pi)
        return self.dp[si][pi]

    def matchRecur2(self, s, p, si, pi):
        if (0 > si or si > len(s)) or (0 > pi or pi > len(p)):
            return False
        if si == len(s) and pi == len(p):
            return True
        if pi + 1 < len(p) and p[pi + 1] == '*':
            return self.dpOrRecur(s, p, si, pi + 2) or \
                ((si < len(s) and pi < len(p) and (s[si] == p[pi] or p[pi] == '.')) and \
                        self.dpOrRecur(s, p, si + 1, pi))
        else:
            return (si < len(s) and pi < len(p) and (s[si] == p[pi] or p[pi] == '.')) and \
                self.dpOrRecur(s, p, si + 1, pi + 1)
