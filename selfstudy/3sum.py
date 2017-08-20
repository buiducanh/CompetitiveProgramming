def threeSum(self, nums):
    nums.sort()
    ans = []
    # fix the first number
    for i in range(len(nums) - 2):
        # duplicate check
        # because checking numbers that start with the same number
        # is duplicative
        if i > 0 and nums[i] == nums[i-1]: continue

        # solve twosum problem from (i + 1, len(nums))
        toFind = -nums[i]
        l = i + 1
        r = len(nums) - 1

        while l < r and nums[l] + nums[r] != toFind:
            while l < r and nums[l] + nums[r] < toFind:
                l += 1
            while l < r  and nums[l] + nums[r] > toFind:
                r -= 1
            if l < r and nums[l] + nums[r] == toFind:
                ans.append((nums[i], nums[l], nums[r]))
                l += 1
                while l < r and nums[l - 1] == nums[l]:
                    l += 1
                r -= 1
                while l < r and nums[r + 1] == nums[r]:
                    r -= 1
    return ans
