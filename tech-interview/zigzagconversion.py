class Solution(object):
    def findMidWayIndex(self, i, numRows, distToNextCol):
        if i % distToNextCol == 0 or i % distToNextCol == distToNextCol - (numRows - 2) - 1:
            return
        ii = i % distToNextCol  - 1
        lengthOfMidWay = numRows - 2
        firstIndexOfMidWay = i + numRows - 1  - ii
        indexRev = lengthOfMidWay - ii - 1
        return firstIndexOfMidWay + indexRev
    def simpleConvert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        step = 1
        index = 0
        result = [''] *numRows
        for c in s:
            result[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(result)
            

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        return self.simpleConvert(s, numRows)
        if numRows == 1 or numRows >= len(s):
            return s
        distToNextCol = 2 * numRows - 2
        res = [[] for i in range(numRows)]
        for i in range(numRows):
            if numRows > 2 and i % distToNextCol != 0 and i % distToNextCol != distToNextCol - (numRows - 2) - 1:
                cur = i
                while cur < len(s):
                    midWay = self.findMidWayIndex(cur, numRows, distToNextCol)
                    res[i].extend([s[cur]])
                    if midWay < len(s):
                        res[i].extend([s[midWay]])
                    cur += distToNextCol
            else:
                cur = i
                while cur < len(s):
                    res[i].extend([s[cur]])
                    cur += distToNextCol
        return "".join(list(map(lambda x: "".join(x), res)))
print(Solution().convert("PayPalIsHiring", 3))
