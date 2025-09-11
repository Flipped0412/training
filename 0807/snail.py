# 달팽이 숫자
# 1부터 N^2 까지 숫자가 시계 방향으로 이루어져 있음
# N크기의 달팽이를 만들어라

def snail(num, row, col):
    end_idx = N
    # 종료 조건
    if num > N*N:
        return

    # 반복
    for up in range(end_idx - row):
        arr[row][col + up] = num
        num += 1
    for left in range(end_idx - row):
        arr[row + left][col + end_idx - 1 - row] = num
        num += 1
    for down in range((end_idx-1-row), row - 1, -1):
        arr[row + end_idx - 1][col + down] = num
        num += 1
    for right in range((end_idx-1-row), row, -1):
        arr[row + right][col] = num
        num += 1

    snail(num, row+1, col+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    snail(1, 0, 0)

    print(f"#{tc}")
    for row in arr:
        print(*row)