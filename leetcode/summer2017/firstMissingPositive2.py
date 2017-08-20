def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        el = nums[i]
        while el - 1 >= 0 and el - 1 < len(nums) and nums[el - 1] != el:
            nums[i], nums[el - 1] = nums[el - 1], nums[i]
            el = nums[i]

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            return i + 1
    return len(nums) + 1
