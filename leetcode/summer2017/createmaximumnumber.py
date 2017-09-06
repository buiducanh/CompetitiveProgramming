class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMaxNumber(nums, k):
            res = []
            maxDrop = max(0, len(nums) - k)
            for num in nums:
                while maxDrop and res and res[-1] < num:
                    res.pop()
                    maxDrop -= 1
                res.append(num)
            return res[:k]

        def dropDigit(nextInd, nums):
            prevInd = nextInd
            nextInd += 1
            while nextInd < len(nums) and nums[prevInd] >= nums[nextInd]:
                prevInd = nextInd
                nextInd += 1

            return nums[:prevInd] + nums[prevInd + 1:], max(prevInd - 1, 0)

        def getMaxNumbers(nums, start, end, dp):
            dp[end] = getMaxNumber(nums, end)
            nextInd = 0
            for i in range(1, end):
                dp[end - i], nextInd = dropDigit(nextInd, dp[end - i + 1])

        def merge(a, b):
            return [max(a, b).pop(0) for _ in range(len(a) + len(b))]

        m, n = len(nums1), len(nums2)
        minL1 = max(0, k - n)
        maxL1 = min(m, k)
        dp1 = [[] for _ in range(k + 1)]
        dp2 = [[] for _ in range(k + 1)]
        getMaxNumbers(nums1, minL1, maxL1, dp1)
        getMaxNumbers(nums2, k - maxL1, k - minL1, dp2)
        return max(merge(dp1[i], dp2[k - i]) for i in range(minL1, maxL1 + 1))


    def maxNumberGreedy(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def comp(a, b):
            while len(a) < len(b):
                a.append(0)
            while len(b) < len(a):
                b.append(0)
            for i in range(len(a)):
                if a[i] < b[i]:
                    return -1
                if a[i] > b[i]:
                    return 1
            return 0

        def getMax(nums, targetLength):
            if not nums or len(nums) == 0 or targetLength <= 0:
                return []
            targetLength = min(targetLength, len(nums))
            canDrop = len(nums) - targetLength
            stack = [i for i in nums[:targetLength]]
            top = 0
            for i in range(1, len(nums)):
                dropped = False
                while top >= 0 and stack[top] < nums[i] and i - top <= canDrop:
                    dropped = True
                    top -= 1
                if i - top > canDrop:
                    while top + 1 < targetLength:
                        top += 1
                        stack[top] = nums[i]
                        i += 1
                    return stack
                top += 1
                if top == targetLength:
                    top = targetLength - 1
                else:
                    stack[top] = nums[i]
            return stack

        def merge(nums1, nums2):
            ind1 = ind2 = 0
            res = []
            i = 0
            while i < len(nums1) + len(nums2):
                if ind1 == len(nums1):
                    res.append(nums2[ind2])
                    ind2 += 1
                elif ind2 == len(nums2):
                    res.append(nums1[ind1])
                    ind1 += 1
                elif nums1[ind1] < nums2[ind2]:
                    res.append(nums2[ind2])
                    ind2 += 1
                elif nums1[ind1] > nums2[ind2]:
                    res.append(nums1[ind1])
                    ind1 += 1
                else:
                    minRemain = min(len(nums1) - ind1, len(nums2) - ind2)
                    check1Larger = comp(
                        nums1[ind1:],
                        nums2[ind2:]
                    )
                    choice1 = False
                    if check1Larger == 1:
                        choice1 = True
                    elif check1Larger == 0:
                        if len(nums1) - ind1 < len(nums2) - ind2:
                            choice1 = True
                    if choice1:
                        while True:
                            res.append(nums1[ind1])
                            ind1 += 1
                            if ind1 >= len(nums1) or nums1[ind1] != nums2[ind2]:
                                break
                            i += 1
                    else:
                        while True:
                            res.append(nums2[ind2])
                            ind2 += 1
                            if ind2 >= len(nums2) or nums1[ind1] != nums2[ind2]:
                                break
                            i += 1
                i += 1
            return res

        maxres = [0 for i in range(k)]
        minL1 = max(0, k - len(nums2))
        maxL1 = min(k, len(nums1))
        for i in range(minL1, maxL1 + 1):
            max_nums1 = getMax(nums1, i)
            max_nums2 = getMax(nums2, k - i)
            tmp = merge(max_nums1, max_nums2)
            if comp(maxres, tmp) == -1:
                maxres = tmp
        return maxres


    def maxNumberRecursionTLE(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def chooseNextMax(pos, start, nums, start_other, other_nums):
            max_ind = min(len(nums), len(nums) - ((k - pos) - (len(other_nums) - start_other) - 1))
            ind = -1
            max_num = -(1 << 31)
            for i in range(max(start, 0), max_ind):
                if max_num < nums[i]:
                    ind = i
                    max_num = nums[i]
            return (max_num, ind)

        def comp(a, b):
            i = 0
            while len(a) < len(b):
                a.append(0)

            while len(b) < len(a):
                b.append(0)

            for i in range(len(a)):
                if a[i] > b[i]:
                    return 1
                elif a[i] < b[i]:
                    return -1
            return 0

        acc_num = []
        max_num = [0 for i in range(k)]
        def chooseRecursion(pos, start1, start2):
            if pos == k:
                for i in range(k):
                    max_num[i] = acc_num[i]
                return

            max1, ind1 = chooseNextMax(pos, start1, nums1, start2, nums2)
            max2, ind2 = chooseNextMax(pos, start2, nums2, start1, nums1)

            if max1 > max2:
                acc_num.append(max1)
                if comp(acc_num, max_num[:pos + 1]) != -1:
                    chooseRecursion(pos + 1, ind1 + 1, start2)
            elif max1 == max2:
                acc_num.append(max1)
                if comp(acc_num, max_num[:pos + 1]) != -1:
                    chooseRecursion(pos + 1, ind1 + 1, start2)
                    chooseRecursion(pos + 1, start1, ind2 + 1)
            else:
                acc_num.append(max2)
                if comp(acc_num, max_num[:pos + 1]) != -1:
                    chooseRecursion(pos + 1, start1, ind2 + 1)

            acc_num.pop()
            return

        chooseRecursion(0, 0, 0)
        return max_num


inp = open("createmaximumnumber.inp")
nums1 = list(map(int, inp.readline().strip().split()))
nums2 = list(map(int, inp.readline().strip().split()))
k = int(inp.readline().strip())
print(Solution().maxNumber(nums1, nums2, k))
