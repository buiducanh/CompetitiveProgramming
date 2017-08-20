class Solution:
    def factorial(self, n):
        ans = 1
        for i in range(n):
            ans = ans * (i + 1) % 1000003
        return ans
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if not A:
            return 0
        ans = 1
        for i in reversed(range(len(A))):
            level = 0
            for j in range(i, len(A)):
                if A[i] > A[j]:
                    level += 1
            ans = (ans + ((level) * self.factorial(len(A) - i - 1)) % 1000003)%1000003
        return ans