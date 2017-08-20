class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        pos = {}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = i
            else:
                if abs(pos[nums[i]] - i) <= k:
                    return True
                else:
                    pos[nums[i]] = i
        return False