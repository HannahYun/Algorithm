import math

n, m = map(int, input().split())
# n! / (m! * (n-m)!)
a = math.factorial(n)
b = math.factorial(m)
c = math.factorial(n-m)
d = b*c

print(a // d)