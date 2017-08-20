class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        minl = -1
        r = -1
        minr = -1
        count = 0
        mapped = {}
        for i in t:
            if i in mapped:
                mapped[i] += 1
            else:
                count += 1
                mapped[i] = 1
        while r + 1 < len(s):
            r += 1
            if s[r] in mapped:
                mapped[s[r]] -= 1
                if mapped[s[r]] == 0:
                    count -= 1
            while count == 0:
                if minl == -1 or r - l < minr - minl:
                    minl = l
                    minr = r
                if s[l] in mapped:
                    mapped[s[l]] += 1
                    if mapped[s[l]] == 1:
                        count += 1
                l += 1
        if minl == -1:
            return ""
        return s[minl:minr + 1]
            