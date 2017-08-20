class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}        
        (l, r) = (0, 0)
        max = 0
        while r < len(s):
            if s[r] not in dic:
                dic[s[r]] = True
            else:
                while s[l] != s[r]:
                    del(dic[s[l]])
                    l += 1
                l += 1
            if r - l + 1 > max:
                max = r - l + 1
            r += 1
        return max
solver = Solution()
print(solver.lengthOfLongestSubstring('abcabcbb'))

