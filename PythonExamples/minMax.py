import numpy
n, m = map(int, raw_input().split())
a = []
for i in range(n):
    a.append(map(int, raw_input().split()))
print numpy.max(numpy.min(a, axis = 1), axis = 0)