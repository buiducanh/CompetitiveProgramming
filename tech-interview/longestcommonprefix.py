class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        s = strs[0]
        minLen = min(map(len, strs))
        i = 0
        res = []
        while i < minLen:
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return ''.join(res)
            res.append(char)
            i += 1
        return ''.join(res)
print(Solution().longestCommonPrefix(['aaaaa', 'aaaa', 'aa']))
