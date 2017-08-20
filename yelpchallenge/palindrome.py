def palin(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    res = 0
    for i in count:
        if count[i] % 2 != 0:
            res += 1
    if len(s) % 2 == 0:
        if res != 0:
            return 'false'
    else:
        if res != 1:
            return 'false'
    return 'true'

s = raw_input()
print palin(s)
