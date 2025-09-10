N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N):
    print(arr[i], end=' ')

print()

for i in range(N - 1, -1, -1):
    print(arr[i], end=' ')