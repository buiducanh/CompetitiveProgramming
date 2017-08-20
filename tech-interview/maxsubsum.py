class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return None
        res = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if cur + nums[i] < nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            if cur > res:
                res = cur
        return res
