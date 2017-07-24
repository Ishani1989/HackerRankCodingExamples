n = int(raw_input())
total = 1

'''
for i in range(1, n+1):
    if n>1:
        total = total*i
print total
'''

def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(n)
