class Solution(object):
    def sol(self, cur, result, candidates, target):
        if target <= 0:
            if target == 0:
                result.append(list(result[0]))
            return
        for i in range(cur, len(candidates)):
            if i > cur and candidates[i] == candidates[i-1]: continue
            result[0].append(candidates[i])
            self.sol(i + 1, result, candidates, target - candidates[i])
            result[0].pop()
    def valid(self, dp, i, t):
        if i < 0:
            return False
        if i == 0:
            return dp[i][t] == 1
        return dp[i][t] != dp[i - 1][t]

    def backtrack(self, curC, candidates, dp, result, curI, curT):
        result[0].append(curC)
        curT -= curC
        curI -= 1
        if curT == 0:
            result.append(list(reversed(result[0])))
            result[0].pop()
            return
        if self.valid(dp, curI, curT):
            self.backtrack(candidates[curI], candidates, dp, result, curI, curT)
            curI -= 1
        while curT > 0 and curI >= 0:
            while curT > 0 and curI > 0 and dp[curI][curT] == dp[curI - 1][curT] or 0 <= curI < len(candidates) - 1 and candidates[curI] == candidates[curI + 1]:
                curI -= 1    
            if self.valid(dp, curI, curT):
                self.backtrack(candidates[curI], candidates, dp, result, curI, curT)
            curI -= 1
        result[0].pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #candidates.sort()
        #result = [[]]
        #self.sol(0, result, candidates, target)
        #return result[1:]
        candidates.sort()
        dp = [[0 for i in range(target + 1)] for j in candidates]
        for i in range(len(candidates)):
            dp[i][0] = 1
        for i in range(len(candidates)):
            for j in reversed(range(1, target + 1)):
                if i > 0:
                    dp[i][j] = dp[i-1][j]
                if j - candidates[i] > 0:
                    dp[i][j] += dp[i - 1][j - candidates[i]]
                elif j - candidates[i] == 0:
                    dp[i][j] += dp[i - 1][j - candidates[i]]
        result = [[]]
        for i in range(len(candidates)):
            if i < len(candidates) - 1 and candidates[i] == candidates[i + 1]: continue
            if i == 0 and dp[i][target] == 1:
                result.append([candidates[i]])
            else:
                if i == 0 or dp[i][target] == dp[i-1][target]: continue
                self.backtrack(candidates[i], candidates, dp, result, i, target)
        return result[1:]


                 
solver = Solution()
print(solver.combinationSum2([10,1,2,7,6,1,5], 8))
print(solver.combinationSum2([1, 1], 2))
print(solver.combinationSum2([2, 2, 2], 2))
print(solver.combinationSum2([3, 1, 3, 5, 1, 1], 8))
