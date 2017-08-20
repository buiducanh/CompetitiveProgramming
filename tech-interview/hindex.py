class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        cnt = [0 for i in range(len(citations) + 1)]
        for i in range(len(citations)):
            cur = min(len(citations), citations[i])
            cnt[cur] += 1
        s = 0
        for i in reversed(range(len(citations) + 1)):
            s += cnt[i]
            if s == i:
                return s
            if s > i and s - cnt[i] <= i:
                return i
        
