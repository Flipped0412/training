def check(row, col):
    # 1. 같은 열에 놓은 적이 있느가?
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 좌상단 대각선에 놓은 적이 이는가? ( \ )
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False

        i -= 1
        j -= j

    # [참고] for 문으로 구현한다면?
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return False
    #

    # 3. 우상단 대각선에 놓은 적이 있는가? ( / )
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        pass
