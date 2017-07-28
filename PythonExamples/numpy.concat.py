import numpy
M, N, P = map(int, raw_input().split())
MList = []
NList = []
for i in range(M):
    MList.append(map(int, raw_input().split()))
for i in range(N):
    NList.append(map(int, raw_input().split()))   
L1 = numpy.array(MList)
L2 = numpy.array(NList)
print numpy.concatenate((L1, L2), axis = 0) 