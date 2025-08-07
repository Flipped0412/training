for test_case in range(1, 11):
    ts = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_max = 0

    temp_sum_diag_r = 0
    temp_sum_diag_l = 0

    for r in range(100):
        temp_sum_row = 0
        temp_sum_col = 0

        temp_sum_diag_r += arr[r][r]
        temp_sum_diag_l += arr[99 - r][r]

        for c in range(100):
            temp_sum_row += arr[r][c]
            temp_sum_col += arr[c][r]

        if temp_sum_row > sum_max:
            sum_max = temp_sum_row
        if temp_sum_col > sum_max:
            sum_max = temp_sum_col

    if temp_sum_diag_r > sum_max:
        sum_max = temp_sum_diag_r
    if temp_sum_diag_l > sum_max:
        sum_max = temp_sum_diag_l

    print(f"#{test_case} {sum_max}")
