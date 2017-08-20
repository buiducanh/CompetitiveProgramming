from sys import stdin, stdout
n, t = map(int, stdin.readline().split())
count = 0
temp = t
while temp > 0:
    count += 1
    temp /= 10
if n < temp: 
    print -1
else:
    stdout.write(str(t))
    for i in range(count, n):
       stdout.write('0') 
    stdout.write("\n")
