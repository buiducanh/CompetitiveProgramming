def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    for i in range(len(nums)):
        num = nums[i]
        ind = num - 1
        while 0 <= ind and ind < len(nums):
            new_ind = nums[ind] - 1
            nums[ind] = 0
            if new_ind != ind:
                ind = new_ind
            else:
                break

        while res - 1 < len(nums) and nums[res - 1] == 0:
            res += 1
    return res
