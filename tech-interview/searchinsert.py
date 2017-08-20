class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while True:
            mid = l + ( r - l + 1) / 2
            if target < nums[mid]:
                r = mid - 1
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            if l > r:
                break
        return l
