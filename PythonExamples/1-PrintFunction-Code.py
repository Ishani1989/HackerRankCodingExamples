from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    m = 1
    total = 0
    for i in reversed(range(n+1)):
#       print(m, total)
        total += i*m
        if i<=9:
            m *= 10
        elif i>9 and i<=99:
            m *= 100
        else:
            m *= 1000

    print (total)