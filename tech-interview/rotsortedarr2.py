def search(nums, target):
    lo = 0
    hi = len(nums)-1
    while lo<=hi:
        mid = lo + (hi-lo)/2
        if nums[mid] < target:
            # when target > mid
            # normally goes to the right, but what about when rotated?
            if nums[mid] >= nums[hi]: # hi < mid < target, rotated, no way to be on left
                lo = mid + 1
            elif target > nums[hi]: # mid < hi < target, no way to be on right
                hi = mid - 1
            else: # mid <= target <= hi must be on right
                lo = mid + 1
        elif nums[mid] == target:
            return True
        else: # target < mid
            # normally goes to left, what abt when rotated?
            if nums[mid] >= nums[hi]: # rotated and target < mid, mid > hi 
                if target <= nums[hi]: # mid > hi >= target
                    lo = mid + 1
                else: # mid > target > hi 
                    hi = mid - 1
            else: # target < mid < hi
                hi = mid - 1
    return False

from sys import stdin
inp = open("rotsortedarr2.in", "r")
# inp = stdin
a = map(int, inp.readline().strip().split())
t = int(inp.readline().strip())
print search(a, t)
