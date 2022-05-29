import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
while(1):    
    if (N % K == 0):
        count += 1
        N = N // K
    else:
        N = N -1
        count += 1
    if N == 1:
        break

print(count)
