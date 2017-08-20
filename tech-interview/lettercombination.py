class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        ans = []
        self.digitMap = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        self.recurSolution(digits, 0, [], ans)
        return ans
    def recurSolution(self, digits, digitIn, word, ans):
        if len(digits) == digitIn:
            ans.append("".join(word))
            return
        for char in self.digitMap[digits[digitIn]]:
            self.recurSolution(digits, digitIn + 1, word + [char], ans)
        return