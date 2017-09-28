def minRotations(s):
    min_char = chr(256)

    for c in s:
        if c < min_char:
            min_char = c

    n = len(s)
    first_min = next(i for i in range(len(s)) if s[i] == min_char, None)
    appended_s = s + s[:first_min + 1]
    cur_min =
    cur_chain = None
    for i in reversed(range(len(s))):


    for i in range(len(s)):
        char = s[i]
        if char < min_char:
            min_char = char
        elif char == min_char:



inp = open("inscription.in")
for line in inp:
    print()
