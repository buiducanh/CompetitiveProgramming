def wordladder(beginWord, endWord, wl):
    path = [set(), set()]
    res = 0
    movingSet, endSet = 0, 1
    levels = [0, 0]
    dq = [{beginWord}, {endWord}]
    while dq[movingSet]:
        if len(path[movingSet]) < len(path[endSet]):
            movingSet, endSet = endSet, movingSet
        path[movingSet].update(dq[movingSet])
        nextSet = set()
        origLen = len(wl)
        while dq[movingSet]:
            word = dq[movingSet].pop()
            for c in xrange(len(word)):
                for t in xrange(26):
                    letter = chr(ord('a') + t)
                    if letter == word[c]:
                        continue
                    trans = word[:c] + letter + word[c+1:]
                    if trans in path[endSet]:
                        return levels[0] + levels[1]
                    if trans in wl:
                        nextSet.add(trans)
                        wl.remove(trans)
        if len(wl) != origLen:
            return 0
        dq[movingSet] = nextSet
        levels[movingSet] += 1
    return 0

def wordladder2(beginWord, endWord, wl):
    time = 0
    wl = list(wl)
    wl.append(beginWord)    
    wl.append(endWord)
    wordlength = len(beginWord)
    mark = [[] for j in xrange(len(wl))]
    for i in range(0, len(wl) - 1):
        for j in range(i+1, len(wl)):
            count = 0
            for k in xrange(wordlength):
                time += 1
                if wl[i][k] == wl[j][k]:
                    count += 1
            if count == wordlength - 1:
                mark[i].append(j)
                mark[j].append(i)
    print time
    from collections import deque
    q = deque()
    q.append(len(wl)-1)
    flag = [True for i in xrange(len(wl))]
    flag[len(wl)-1] = False
    level = [0 for i in xrange(len(wl))]
    while q:
        cur = q.pop()
        for i in mark[cur]:
            time += 1
            if flag[i]:
                flag[i] = False
                level[i] = level[cur] + 1
                if i == len(wl) - 2:
                    print time
                    return level[i] + 1
                q.append(i)
    return 0

from sys import stdin
inp = open("wordladder.in", "r")
# inp = stdin
be = inp.readline().strip()[1:-1]
en = inp.readline().strip()[1:-1]
wl = inp.readline().strip()[2:-2].split("\",\"")
wl = set(wl)
print wordladder(be, en, wl)
