# f(N) = f(N-2)*2 + f(N-1)

def solve(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3

    return solve(N-20)*2 + solve(N-10)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = solve(N)
    print(f'#{tc} {result}')
