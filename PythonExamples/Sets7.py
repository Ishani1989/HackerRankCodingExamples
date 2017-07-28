"""TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

 len(set(A))  
 len(otherSets)  

Output Format

Output the sum of elements in set .

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38"""


n = input()
A = set(map(int, raw_input().split())) 
N = input()
total=0
for i in range(N):
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

for element in A:
    total += element
print total