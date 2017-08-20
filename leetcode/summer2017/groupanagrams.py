class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        return group.values()
