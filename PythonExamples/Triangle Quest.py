for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**(i)-1)/9)**2




for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i-1)/9)*i


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a = raw_input().split()
A = list(permutations(a[0], 2))
A.sort()
for i in A:
    print i[0]+ i[1]



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
