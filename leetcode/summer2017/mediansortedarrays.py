A = list(map(int, raw_input().strip().split()))
B = list(map(int, raw_input().strip().split()))

def findMedian(A, B):
    n = len(A)
    m = len(B)

    if n > m:
        A, B, n, m = B, A, m, n

    median = None

    if n == 0 and m == 0:
        return

    if n == 0:
        return (B[int(round((m | 1) / 2.0)) - 1] + B[int(round(m / 2.0)) - 1]) / 2.0

    imin = 0
    imax = n

    is_odd = (m + n) % 2

    while True:
        i = (imin + imax) / 2
        j = (m + n + 1)/ 2 - i

        if i == 0:
            if B[j - 1] <= A[i]:
                if is_odd:
                    median = B[j - 1]
                else:
                    median = B[j - 1]
                    if j != m:
                        median += min(A[i], B[j])
                    else:
                        median += A[i]
                    median /= 2.0
            else:
                imin = i + 1
                continue
            break

        if i == n:
            if A[i - 1] <= B[j]:
                if is_odd:
                    if j != 0:
                        median = max(A[i - 1], B[j - 1])
                    else:
                        median = A[i - 1]
                else:
                    if j != 0:
                        median = max(A[i - 1], B[j - 1])
                    else:
                        median = A[i - 1]
                    median += B[j]
                    median /= 2.0
            else:
                imax = i - 1
                continue
            break


        if A[i - 1] <= B[j] and B[j - 1] <= A[i]:
            if is_odd:
                median = max(A[i - 1], B[j - 1])
            else:
                median = (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2.0
            break
        elif B[j - 1] > A[i]:
            imin = i + 1
        elif A[i - 1] > B[j]:
            imax = i - 1

    return median

print(findMedian(A, B))
