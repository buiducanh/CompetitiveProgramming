def arrayForce2(a,b,n,mod):
    list = [a, b]
    m = {a: [b]}
    count = {a: 0, b: 0}
    count[a] += 1
    count[b] += 1
    for i in xrange(n - 2):
        x = (list[-1] + list[-2]) % mod
        if list[-1] in m:
            if x in m[list[-1]]:
                count[list[-1]] -= 1
                break
            m[list[-1]].append(x)
        else:
            m[list[-1]] = [x]
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
        list.append(x)
    print list
    print count
    print m
    length = len(list) - 1
    periods = n / length
    remainder = n % length
    print length, periods, remainder
    for key in count:
        count[key] *= periods
    print count
    for i in xrange(remainder):
        count[list[i]] += 1
    print count
    res = 0
    for key in count:
        res += count[key]**2
    return res  

def arrayForce(a, b, n, mod):
    list = [a, b]
    m = {a: 0, b: 0}
    m[a] += 1
    m[b] += 1
    for i in xrange(n - 2):
        x = (list[-1] + list[-2]) % mod
        list.append(x)
        if x in m:
            m[x] += 1
        else:
            m[x] = 1
    res = 0
    for i in m.keys():
        res += m[i]**2
    return res

for i in xrange(int(raw_input().strip())):
    a, b, n, mod = map(int, raw_input().strip().split())
    res1 =  arrayForce(a, b, n, mod)
    res2 =  arrayForce2(a, b, n, mod)
    if res1 != res2:
        print a, b, n, mod, res1, res2
