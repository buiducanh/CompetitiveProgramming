class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rable = 0
        for i in range(len(nums)):
            if rable < i:
                return False
            rable = max(rable, i + nums[i])
        return True
