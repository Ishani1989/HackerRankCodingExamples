# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
from decimal import *

n = int(raw_input())
d = raw_input().split()
m = int(raw_input())
indices = list()
c=0
l = list(combinations(d, m))
for i in l:
    if 'a' in i:
        c=c+1
print round(Decimal(c)/Decimal(len(l)), 12)
   

    
        