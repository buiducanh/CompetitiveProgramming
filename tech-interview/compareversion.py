class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = map(int, version1.split("."))
        ver2 = map(int, version2.split("."))
        if len(ver1) < len(ver2):
            ver1.extend([0 for i in range(len(ver2) - len(ver1))])
        else:
            ver2.extend([0 for i in range(len(ver1) - len(ver2))])
        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
        return 0
