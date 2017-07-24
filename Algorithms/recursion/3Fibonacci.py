# Fibonacci using iteration

n = int(raw_input())
'''
i = 0
j = 1
print i,
for x in range(n-1):
    print j,
    temp = j
    j = i + j
    i = temp'''

def fibonacci(n):
    #print "fibo("+str(n)+")"
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print fibonacci(n)