class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not org and seqs:
            return False
        if org and not seqs:
            return False
        maxi = max(org)
        edges = [[False for i in range(maxi + 1)] for i in range(maxi + 1)]
        for seq in seqs:
            if seq[0] > maxi: return False

            for i in range(1, len(seq)):
                if seq[i] > maxi:
                    return False
                edges[seq[i - 1]][seq[i]] = True

        cur = org[0]
        for i in range(1, len(org)):
            if not edges[cur][org[i]]:
                return False
            for j in range(i):
                if edges[org[i]][org[j]]:
                    return False
            cur = org[i]
        return True
