def leveltraverse(b):
    height = int(log(2, len(b))) 
    res = []
    for i in range(height, -1, -1):
        cur = 2**i - 1
        res.append(b[cur: cur + (cur + 1) + 1] )
    return res
        
