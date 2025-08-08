for test_case in range(1, 11):
    tc = int(input())
    ladder = list(map(int, input().split()))
    check = True

    for row in range(100):
        if ladder[row][0] == 1:
            start_row = row
            while check:
                for col in range(100):
                    if ladder[row + 1][col] == 1:  # 우 확인되면
                        for move_row in range(100):
                            ladder[row + move_row][col]
                            if ladder[row + move_row][col] == 0:
                                row = row + move_row
                                break
                    if ladder[row -1 ][col] == 1:  # 좌 확인되면
                        for move_row in range(100):
                            ladder[row - move_row][col]
                            if ladder[row - move_row][col] == 0:
                                row = row - move_row
                                break
                    if ladder[row][col + 1] == 2:
                        result = start_row
                        check = False
                        break
    print(f"#{test_case} {result}")
    


# for di, dj in [[-1, 0], [1, 0]]:
#     new_row, new_col = row + di, col + dj
#     if ladder[new_row][new_col] == 1:
#         move_row, move_col = new_row, new_col