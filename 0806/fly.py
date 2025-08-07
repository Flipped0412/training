T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for row in range(N-M+1):
        for col in range(N-M+1):
            temp_sum = 0
            for smash_row in range(M):
                for smash_col in range(M):
                    temp_sum += arr[row+smash_row][col+smash_col]
            if temp_sum > max_sum:
                max_sum = temp_sum
    
    print(f"#{test_case} {max_sum}")
