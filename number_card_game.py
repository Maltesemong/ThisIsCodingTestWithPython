import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result_list = []
for i in range(N):
    data = map(int, input().split())
    result_list.append(min(data))

print(max(result_list))
