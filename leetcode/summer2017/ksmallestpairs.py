A = list(map(int, raw_input().strip().split()))
B = list(map(int, raw_input().strip().split()))
k = int(raw_input())

import heapq

def kSmallestPairs(nums1, nums2, k):
    if len(nums1) == 0 or len(nums2) == 0:
        return []

    pairs = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
    heapq.heapify(pairs)
    result = []
    for i in range(k):
        if len(pairs) == 0:
            break
        next_val = heapq.heappop(pairs)
        result.append((nums1[next_val[1]], nums2[next_val[2]]))
        ind1 = next_val[1]
        ind2 = next_val[2] + 1
        if ind2 < len(nums2):
            heapq.heappush(pairs, (nums1[ind1] + nums2[ind2], ind1, ind2))
    return result



print(kSmallestPairs(A, B, k))
