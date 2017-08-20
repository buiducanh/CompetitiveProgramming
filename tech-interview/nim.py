from sys import stdin
def nim(n):
    if n % 4 == 0:
        return False
    else:
        return True

# inp = open("nim.in", "r")
inp = stdin
n = int(inp.readline())
print nim(n)
