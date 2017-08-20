def search(nums, target):
    lo = 0
    hi = len(nums)-1
    while lo<=hi:
        mid = lo + (hi-lo)/2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            # when target > mid
            # Once mid > hi, everytime rotated, mid and hi reduce as well
            # --> always rotated when mid > hi
            if nums[mid] > nums[hi]: 
                # since rotated, left side sorted, but target bigger so left can't
                lo = mid + 1
            elif target > nums[hi]: 
                # mid < hi < target, no way to be on right
                hi = mid - 1
            else: 
                # mid < target <= hi must be on right
                lo = mid + 1
        else:
            # target < mid
            if nums[mid] > nums[hi]: 
                # rotated and target < mid
                if target <= nums[hi]: # mid > hi >= target
                    lo = mid + 1
                else: # mid > target > hi 
                    hi = mid - 1
            else: # target < mid < hi
                hi = mid - 1
    return -1

from sys import stdin
inp = open("rotsortedarr.in", "r")
# inp = stdin
a = map(int, inp.readline().strip().split())
t = int(inp.readline().strip())
print search(a, t)
