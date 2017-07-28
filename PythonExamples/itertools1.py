# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = raw_input().split()
sum=0
for i in range(int(k)):
    l = map(int, raw_input().split())
    mx = max(l)
    sum = sum+(mx**2)
print sum%int(m)