# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math
a = raw_input()
print a
x = float(a[0])
y = float((a[1])[:-1])
print (math.sqrt((x*x)+(y*y)))
print cmath.phase(complex(x, y))



# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math
input = raw_input()
#rint input

prevNegSign = False;
prevDigit = False;

arr = []

/*r c in input:    
    #print c
    if c.isdigit(): 
        prevDigit = True 
        if prevNegSign == True:
            arr.append(-1 * int(c))
            prevNegSign = False
        elif prevNegSign == False:
            arr.append(c)
    else:
        if c== '-':
            prevNegSign = True
        elif c == '+':
            prevDigit = False
*/     
x = int(arr[0])
y = int(arr[1])
print (math.sqrt((x*x)+(y*y)))
print cmath.phase(complex(x, y))

