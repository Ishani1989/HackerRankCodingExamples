# 7/19/2017 reverse a string
# Approach 1 - using interation
import sys
'''
input_str = raw_input()
namelist = []
i = len(input_str)-1
while i>=0:
    sys.stdout.write(input_str[i])
    i-=1
'''
# Approach 1 - using recursion

input_str = raw_input()

def revStr(str):
    print 'revStr('+ str +')'
    if len(str)< 1:
        return 0
    elif len(str)== 1:
        return str
    elif len(str)>1:
        return revStr(str[1:])+str[0]
print revStr(input_str)
