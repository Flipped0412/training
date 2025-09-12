def snail(num, row, col):
    # 종료 조건
    if num > N * N:
        return

    # 현재 레이어 경계
    top, left = row, col
    bottom, right = N - 1 - row, N - 1 - col

    # 위쪽 가로 (좌 -> 우)
    for c in range(left, right + 1):
        arr[top][c] = num
        num += 1

    # 오른쪽 세로 (위 -> 아래)
    for r in range(top + 1, bottom + 1):
        arr[r][right] = num
        num += 1

    # 아래쪽 가로 (우 -> 좌) — 한 줄 레이어면 생략
    if top < bottom:
        for c in range(right - 1, left - 1, -1):
            arr[bottom][c] = num
            num += 1

    # 왼쪽 세로 (아래 -> 위) — 한 칸 레이어면 생략
    if left < right:
        for r in range(bottom - 1, top, -1):
            arr[r][left] = num
            num += 1

    snail(num, row + 1, col + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    snail(1, 0, 0)

    print(f"#{tc}")
    for row in arr:
        print(*row)
