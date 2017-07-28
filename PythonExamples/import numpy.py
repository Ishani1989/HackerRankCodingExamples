import numpy
N, M = map(int, raw_input().split())

l =[]
for i in range(N+1):
    l.append(map(int, raw_input().split())) 

a = numpy.array(l[0], int)
b = numpy.array(l[1], int)

for i in [a+b,a-b,a*b,a/b,a%b, a**b]:
    print '['+ str(i)+']'
