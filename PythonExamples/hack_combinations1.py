# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import combinations
a = raw_input().split()
A = list(combinations(a[0],int(a[1])))
M = list()
B =list( a[0])
B.sort()
for i in B:
    print (i)
for x in A:
    temp = list(x)
    temp.sort()
    M.append(temp)

M.sort()

for x in M:
    for y in x:
        print (y,end='')
    print()





for k in range(1,int(a[1])+1):
    A = list(combinations(a[0], k))
    for x in A:
        for i  in range(len(x)):
            #print(x[i],end='')
            str+=x[i]
        #print('') 
        l.append(str)
        l.sort()
        str=''
        
print(l)


