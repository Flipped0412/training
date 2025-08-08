for test_case in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for col in range(100):
        if ladder[0][col] == 1:
            temp_col = col
            start_col = col
            check = True

            while check:
                for row in range(99):
                    if temp_col < 99 and ladder[row][temp_col + 1] == 1:  # 우 확인되면
                        while temp_col < 99 and ladder[row][temp_col + 1] == 1:
                            temp_col += 1
                        row += 1
                    elif temp_col > 0 and ladder[row][temp_col - 1] == 1:  # 좌 확인되면
                        while temp_col > 0 and ladder[row][temp_col - 1] == 1:
                            temp_col -= 1
                        row += 1
                    else:
                        row += 1

                    if row == 99 and ladder[row][temp_col] == 2:
                        result = start_col
                        check = False
                        break
                    elif row == 99:
                        check = False

    print(f"#{tc} {result}")