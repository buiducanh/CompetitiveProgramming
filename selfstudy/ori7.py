def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return [a, b]

a = 15
b = 3
print(swap(a, b))
