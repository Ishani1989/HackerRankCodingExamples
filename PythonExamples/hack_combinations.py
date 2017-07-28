from itertools import combinations

s , n  = raw_input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print ''.join(j)




# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
from itertools import combinations
input = raw_input().split()


for i in range(1, int(input[1])+1):
    l = list(combinations(input[0],i))
    l.sort()
    #print (l)
    
    for x in l:
        temp_l = []
        for y in x:
            temp_l.append(y)
        temp_l.sort()
        
        temp_l2 = []
        str = ''
        for z in temp_l:
            #print (z,end='')
            str += z;
        #print()
        temp_l2.append(str)
        temp_l2.sort()
        print ('***********')
        print (temp_l2)
        
        for w in temp_l2:
            print (w)

    
The method join() returns a string in which the string elements of sequence have been joined by str separator.

Syntax
Following is the syntax for join() method:

str.join(sequence)