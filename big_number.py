import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = []
A = list(map(int, input().split()))
max_A = max(A)
result = max_A * K * (M // K)
A.remove(max_A)
max_A = max(A)
result += max_A * (M - M // K * K)
print(result)
