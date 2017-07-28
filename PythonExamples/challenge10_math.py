"""Task 
You are given a complex . Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number .

Output Format

Output two lines: 
The first line should contain the value of . 
The second line should contain the value of .

Sample Input

  1+2j
Sample Output

 2.23606797749979 
 1.1071487177940904"""




# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math
input = raw_input()

prevNegSign = False;
prevDigit = False;

arr = []

if input[0] == '-':
    input = input[1:len(input)]
    prevNegSign=True    
    
if '+' in input:
    arr = input.split('+')
    if prevNegSign==True:
        arr[0] = int(arr[0]) * -1 
    arr[1] = arr[1][:-1]

elif '-' in input:
    arr = input.split('-')
    if prevNegSign==True:
        arr[0] = int(arr[0]) * -1
    if 'j' in arr[1]:
        arr[1] = arr[1][:-1]
        arr[1] = int(arr[1]) * -1
           
x = int(arr[0])
y = int(arr[1])
print (math.sqrt((x*x)+(y*y)))
print cmath.phase(complex(x, y))

