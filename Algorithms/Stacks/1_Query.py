# Enter your code here. Read input from STDIN. Print output to STDOUT

n = long(raw_input())
max = 0
stack = []
index = 0
for i in range(n):
    temp = map(long, raw_input().split())
    if temp[0]==1:
        stack.append(temp[1])
        index += 1
        if temp[1]>max:
            max = temp[1]
    elif temp[0]==2:
        stack.pop(index-1)
    elif temp[0]==3:
        #print count,
        print max
        #count+=1
