# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
a = list(raw_input())
a.sort()

l = []
l1 = [ ] 
l2 = []
l3 = []

y = map(lambda x : l.append(x) if x.isdigit() and int(x)%2==0 else l3.append(x) if x.isdigit() and int(x)%2!=0 else  l1.append(x) if x.isupper() else l2.append(x), a)

final_l =  l2+ l1 + l3 + l
print(*final_l,sep='')



-----------------------------------------------------------------------------------------------------------------------------
print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')