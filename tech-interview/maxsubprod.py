class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sol(l, r, nums):
            res = nums[l]
            culm = [nums[l], nums[l]]
            for i in range(l + 1, r):
                if culm[0] * nums[i] < culm[0]:
                    culm[0] = nums[i]
                culm[1] *= nums[i]
                if culm[1] > culm[0]:
                    culm[0] = culm[1]
                if culm[0] > res:
                    res = culm[0]
            if res < nums[r - 1]:
                res = nums[r -  1]
            culm = [nums[r - 1], nums[r - 1]]
            for i in reversed(range(l, r - 1)):
                if culm[0] * nums[i] < culm[0]:
                    culm[0] = nums[i]
                culm[1] *= nums[i]
                if culm[1] > culm[0]:
                    culm[0] = culm[1]
                if culm[0] > res:
                    res = culm[0]
            return res
        nums.append(0)
        res = nums[0]
        cur = 0
        while cur < len(nums) and nums[cur] == 0:
            cur += 1
        i = cur
        while i < len(nums):
            if nums[i] == 0 and i - 1 >= 0:
                if res < 0 and i < len(nums)  - 1:
                    res = 0
                res = max(res, sol(cur, i, nums))
                while i < len(nums) and nums[i] == 0:
                    i += 1
                cur = i
            else:
                i += 1
        return res
