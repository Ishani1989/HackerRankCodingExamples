""" Intersection of sets
"""# Enter your code here. Read input from STDIN. Print output to STDOUT


M = int(raw_input())
eng = set(map(int, raw_input().split()))
N = int(raw_input())
fr= set(map(int, raw_input().split()))
s=set()
s.update(eng)
t= set()
t.update(fr)
u= set()
u = s.intersection(t)
print len(u)