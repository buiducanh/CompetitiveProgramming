# inp = open("2.in", "r")
import sys
inp = sys.stdin
n = int(inp.readline().strip())
prices = map(int, inp.readline().strip().split())
days = int(inp.readline().strip())

def qsort(nums, l, r):
  if r <= l:
    return
  mid = (r - l)/2 + l
  i = l
  j = r
  while True:
    while i < mid and nums[i] < nums[mid]:
      i += 1
    while j > mid and nums[j] >= nums[mid]:
      j -= 1
    if i <= j:
      if i < j:
        nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1
    if i > j:
      break
  qsort(nums, l, j)
  qsort(nums, i, r)

qsort(prices, 0, len(prices) - 1)

def bin_search_largest(nums, val, l, r):
  mid = (r - l + 1)/2 + l
  if nums[mid] <= val:
    l = mid
  if nums[mid] > val:
    r = mid - 1
  if l < r:
    return bin_search_largest(nums, val, l, r)
  elif l == r and nums[l] <= val:
    return l
  else:
    return -1

for i in range(days):
  coin = int(inp.readline().strip())
  index = bin_search_largest(prices, coin, 0, n - 1)
  print(index + 1)

