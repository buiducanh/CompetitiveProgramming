class Solution(object):
    def left(self, nums, target):
        l = 0
        r = len(nums) - 1
        while True:
            mid = l + ( r - l) / 2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                r = mid
            if l >= r:
                break
        if l >= len(nums) or nums[l] != target:
            return -1
        return l
    def right(self, nums, target):
        l = 0
        r = len(nums) - 1
        while True:
            mid = l + ( r - l + 1) / 2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                l = mid
            if l >= r:
                break
        if l >= len(nums) or nums[l] != target:
            return -1
        return l    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.left(nums, target), self.right(nums, target)]
                
