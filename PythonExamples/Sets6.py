n = input()
A = set(map(int, raw_input().split())) 
N = input()
total=0
for i in range(N*2):
    x = raw_input().split(" ")
    y = set(map(int, raw_input().split()))
    action=x[0]
    if action=="intersection_update":
        A.intersection_update(y)
    elif action=="update":
        A.update(y)
    elif action=="symmetric_difference_update":
        A.symmetric_difference_update(y)
    elif action=="difference_update":
        A.difference_update(y)
for p in s:
    total += p
print total