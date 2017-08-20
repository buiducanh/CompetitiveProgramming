word = raw_input()

cur = 0

ans = 0

for i in word:
    ch = ord(i) - 97
    if ch < cur:
        fw = 26 - cur + ch
        bw = cur - ch
        ans += min(fw, bw)
        cur = ch
    elif ch > cur:
        bw = 26 - ch + cur
        fw = ch - cur
        ans += min(fw, bw)
        cur = ch

print(ans)

