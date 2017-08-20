class Solution(object):
    def compareAnagram(self, a, b):
        cntA = [0 for i in range(26)]
        cntB = [0 for i in range(26)]
        for c in a:
            cntA[ord(c) - ord('a')] += 1
        for c in b:
            cntB[ord(c) - ord('a')] += 1
        for i in range(26):
            if cntA[i] > cntB[i]:
                return 1
            elif cntA[i] < cntB[i]:
                return -1
        return 0

    def merge(self, a, b):
        indexA = 0
        indexB = 0
        result = []
        while indexA < len(a) and indexB < len(b):
            if self.compareAnagram(a[indexA], b[indexB]) != -1:
                result.append(b[indexB])
                indexB += 1
            else:
                result.append(a[indexA])
                indexA += 1
        if indexA != len(a):
            return result.extend(a[indexA:])
        if indexB != len(b):
            return result.extend(b[indexB:])


    def recurSol(self, strs):
        sortedListA = self.recurSol(strs[:len(strs) / 2])
        sortedListB = self.recurSol(strs[len(strs) / 2:])
        return self.merge(sortedListA, sortedListB)

    def anagramCnt(self, a):
        cntA = [0 for i in range(26)]
        for c in a:
            cntA[ord(c) - ord('a')] += 1
        return cntA
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            ordered = "".join(sorted(i))
            if not dic.has_key(ordered):
                dic[ordered] = []
            dic[ordered].append(i)
        result = []
        for i in dic:
            result.append(sorted(dic[i]))
        return result

