class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        res_list = [1]
        mul = [2, 3, 5]
        cur = 1
        n -= 1
        mul_index = [0, 0, 0]
        choose_index = [0, 0, 0]
        while n > 0:
            new_muls = []
            for i in range(3):
                while res_list[mul_index[i]] * mul[i] <= cur:
                    mul_index[i] += 1
                new_muls.append(res_list[mul_index[i]] * mul[i])
            res_list.append(min(new_muls))
            cur = res_list[-1]
            n -= 1
        return res_list[-1]
