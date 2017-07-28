# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
is_valid = True
for i in range(n):
    try:
        re.compile(raw_input())
        is_valid = True
    except re.error:
        is_valid = False
    print is_valid