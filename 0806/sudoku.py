T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    check_num = list(range(1,10))
    check = 1

    for row in range(9):
        check_list_row = []
        check_list_col = []
        for col in range(9):
            check_list_row.append(arr[row][col])
            check_list_col.append(arr[col][row])
            if row % 3  == 0 and col % 3 == 0:
                check_list_square = []
                for square_row in range(3):
                    for square_col in range(3):
                        check_list_square.append(arr[row+square_row][col+square_col])

        check_list_row = sorted(check_list_row)
        check_list_col = sorted(check_list_col)
        check_list_square = sorted(check_list_square)

        if check_list_row != check_num or check_list_col != check_num or check_list_square != check_num:
            check = 0
            break

    print(f"#{test_case} {check}")