def rectA(n,m,x,y):
    return (abs(m - y) * abs(x - n))
class Solution(object):


    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        n = m = x = y = 0
        if A <= E <= C:
            n = E
            x = min(C, G)
        elif E <= A <= G:
            n = A
            x = min(C, G)
        if B <= F <= D:
            m = F
            y = min(D, H)
        elif F <= B <= H:
            m = B
            y = min(D, H)
        return rectA(A, B, C, D) + rectA(E, F, G, H) - rectA(n, m, x, y)